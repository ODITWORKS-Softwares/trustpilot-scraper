# trustpilot-scraper
trustpilot business listing data scraper using Scrapy &amp; Selenium
This is a Scrapy-based web scraper designed to extract business data from Trustpilot using category-specific endpoints. It reads from a CSV file containing category identifiers and automatically crawls paginated business listings within each sub-category.

📦 Features
🔍 Scrapes business data by category and sub-category

📄 Reads input from main_categories.csv (includes sub_category_id, main_category, sub_category)

🧾 Outputs:

Business name

TrustScore & stars

Number of reviews

Address (city, zip, country)

Website, email, phone

Logo URL

Multiple assigned categories

🔁 Handles automatic pagination until all pages are scraped

🧩 JSON endpoint scraping for fast, structured results

✅ Clean item structure using Scrapy's Item system

📁 Project Structure
  trustpilot_scraper/
├── items.py              # Defines DataIteam for output
├── spiders/
│   └── product_scraper.py # Main spider logic
├── output/
│   └── main_categories.csv # CSV input with sub_category_id and labels
├── pipelines.py
├── settings.py
└── run_debug_spider.py   # Optional debug entry

🛠️ Setup Instructions
  git clone https://github.com/yourusername/trustpilot_scraper.git
  cd trustpilot_scraper

  1. Clone the repository:
     git clone https://github.com/yourusername/trustpilot_scraper.git
      cd trustpilot_scraper
  2. Install dependencies:
       pip install -r requirements.txt
  3. Prepare your input CSV:
     sub_category_id,main_category,sub_category
      car-rental,Transportation,Car Rental
      financial-services,Business,Financial Services
  4. Run the spider:
     scrapy crawl products -o trustpilot_data.json
     scrapy crawl products -o trustpilot_data.csv

How It Works
  For each row in main_categories.csv, the spider constructs a Trustpilot JSON API URL using the sub_category_id.
  It parses the JSON response, extracts business details, and continues paginating until all pages for that sub-category are scraped.

📦 Output Fields
  Each business item includes:

  main_category
  
  sub_category
  
  businessName
  
  reviewPageName
  
  stars
  
  trustScore
  
  numberOfReviews
  
  logoUrl
  
  address, city, zipCode, country
  
  website, email, phone
  
  category_data: a dictionary of assigned categories

  ⚠️ Disclaimer
This tool is intended for educational and research purposes only. Scraping Trustpilot may violate their Terms of Service and should be done responsibly. Always use appropriate headers, respect rate limits, and consider their API.





