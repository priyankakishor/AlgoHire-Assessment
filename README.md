# AlgoHire-Assessment

# Project Overview
This project is a Python-based web scraper built using Selenium WebDriver.The goal is to scrape laptop product data from the webscraper.io test site,extract specific fields, and save the results into a structured JSON file.

# Features
•	Extracts the following fields for each laptop:
  •	title – Name of the laptop
  •	price – Listed price (e.g., $1,499.00)
  •	rating – Number of stars, taken from data-rating attribute
  •	reviews_count – Total number of reviews (reviewCount span)
  •	product_url – Full link to product detail page
•	Handles pagination automatically across all pages.
•	Saves results into output.json with proper formatting.
•	Works with both local ChromeDriver or auto-downloads one using webdriver-manager.

# Tech Stack
  •	Python 3.10.11
  •	Selenium WebDriver
  •	ChromeDriver
  •	webdriver-manager (fallback if local driver is missing)
  •	JSON for data storage

# Project Structure
project/
│── main.py             # Main scraper script
│── requirements.txt    # Python dependencies
│── README.md           # Documentation
│── output.json         # Scraped data (generated after run)
│── chromedriver.exe    # (Optional) Local ChromeDriver

# Setup Instructions
1. Install Dependencies
   pip install -r requirements.txt
2. ChromeDriver Setup
   If chromedriver.exe is placed in the project folder, the script will use it.
   If not, webdriver-manager will automatically download the correct driver.

# Run the Project
Run the scraper with:
  python main.py
The script will open the laptops listing page.
Scrape all products across multiple pages.
Save the extracted data into output.json.

# Example Output
 [
  {
    "title": "Asus VivoBook...",
    "price": "$295.99",
    "rating": 3,
    "reviews_count": 14,
    "product_url": "https://webscraper.io/test-sites/e-commerce/allinone/product/60",
    "description": "Asus VivoBook X441NA-GA190 Chocolate Black, 14\", Celeron N3450, 4GB, 128GB SSD, Endless OS, ENG kbd"
  },
  {
    "title": "Prestigio Smar...",
    "price": "$299",
    "rating": 2,
    "reviews_count": 8,
    "product_url": "https://webscraper.io/test-sites/e-commerce/allinone/product/61",
    "description": "Prestigio SmartBook 133S Dark Grey, 13.3\" FHD IPS, Celeron N3350 1.1GHz, 4GB, 32GB, Windows 10 Pro + Office 365 1 gadam"
  },
  ]


# Conclusion
This project demonstrates:
  •	Automated scraping with Selenium.
  •	Extracting structured data (title, price, rating, reviews, URL).
  •	Handling pagination.
  •	Saving results in JSON format
It can be extended easily to other categories or websites.


