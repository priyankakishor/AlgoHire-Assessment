import json
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urljoin
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

def init_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    project_dir = os.path.dirname(os.path.abspath(__file__))
    local_driver_path = os.path.join(project_dir, "chromedriver.exe")
    if os.path.exists(local_driver_path):
        print("Using local ChromeDriver from project folder")
        service = Service(local_driver_path)
    else:
        print("chromedriver.exe not found in project folder. Installing with webdriver-manager...")
        from webdriver_manager.chrome import ChromeDriverManager
        service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)
    return driver

def scrape_list(driver):    
    driver.get(BASE_URL)
    product_links = []
    while True:
        products = driver.find_elements(By.CSS_SELECTOR, ".thumbnail")
        for product in products:
            # Title + URL
            title_el = product.find_element(By.CSS_SELECTOR, "a.title")
            title = title_el.text.strip()
            href = title_el.get_attribute("href")
            product_url = urljoin("https://webscraper.io", href)
            # Price details
            price = product.find_element(By.CSS_SELECTOR, ".price").text.strip()

            # Reviews details
            try:              
                reviews_el = product.find_element(By.CSS_SELECTOR, ".ratings .review-count span[itemprop='reviewCount']")
                reviews_count = int(reviews_el.text.strip())
            except:
                reviews_count = 0
            
            # Rating Details
            try:
                rating_el = product.find_element(By.CSS_SELECTOR, ".ratings p[data-rating]")
                rating = int(rating_el.get_attribute("data-rating"))
            except:
                rating = 0

            product_links.append({
                "title": title,
                "price": price,
                "rating": rating,
                "reviews_count": reviews_count,
                "product_url": product_url
            })

        # handling Pagination
        try:
            next_btn = driver.find_element(By.CSS_SELECTOR, "li.next > a")
            driver.execute_script("arguments[0].click();", next_btn)
            time.sleep(1)
        except NoSuchElementException:
            break
    return product_links

def scrape_details(driver, product_links):
    products_data = []
    for item in product_links:
        driver.get(item["product_url"])
        try:
            desc_el = driver.find_element(By.CSS_SELECTOR, ".description")
            description = desc_el.text.strip()
        except NoSuchElementException:
            description = ""
        item["description"] = description
        products_data.append(item)
    return products_data

def save_json(data, filename="output.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    driver = init_driver()
    product_links = scrape_list(driver)
    products_data = scrape_details(driver, product_links)

    driver.quit()
    save_json(products_data)
    print(f"Scraping completed {len(products_data)} products saved to output.json")


if __name__ == "__main__":
    main()
