from scrapy import Spider
import scrapy
import csv
import os
import json
from trustpilot_scraper.items import DataIteam

class ProductScraperSpider(Spider):
    name = "products"
    allowed_domains = ["trustpilot.com"]
    category_id=""

    def start_requests(self):
        csv_path ='C:\\scraper\\trustpilot_scraper\\output\\main_categories.csv'  #os.path.join(os.path.dirname(__file__), '../../../output/main_categories.csv')
        with open(csv_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.category_id = row['sub_category_id']
                _url = f"https://www.trustpilot.com/_next/data/categoriespages-consumersite-2.718.0/categories/{self.category_id}.json?categoryId={self.category_id}"
                url = _url
                yield scrapy.Request(url=url, callback=self.parse_page, meta={'main_category': row['main_category'], 'sub_category': row['sub_category']})

    def parse_page(self, response):
        main_category = response.meta.get('main_category')
        sub_category = response.meta.get('sub_category')
        data = json.loads(response.text)
        page_data = data.get("pageProps", {})
        current_page = page_data.get("page", 1)
        max_pages = page_data.get("seoData", {}).get("maxPages", 1)

        # Extract business data
        businesses = page_data.get("businessUnits", {}).get("businesses", [])
        for biz in businesses:
            location = biz.get("location", {})
            contact = biz.get("contact", {})
            categories = biz.get("categories", [])
            category_data = {
                f"category_{i+1}_name": cat.get("displayName")
                for i, cat in enumerate(categories)
            }
            item = DataIteam()
            item['main_category']= main_category
            item['sub_category']= sub_category
            item['businessName']= biz.get("displayName")
            item['reviewPageName']= biz.get("identifyingName")
            item['stars']= biz.get("stars")
            item['trustScore']= biz.get("trustScore")
            item['numberOfReviews']= biz.get("numberOfReviews")
            item['logoUrl']= biz.get("logoUrl")
            item['address']= location.get("address")
            item['city']= location.get("city")
            item['zipCode']= location.get("zipCode")
            item['country']= location.get("country")
            item['website']= contact.get("website")
            item['email']= contact.get("email")
            item['phone']= contact.get("phone").replace("=", "")
            item['category_data'] = category_data
            yield item
             

        # Handle pagination automatically if not covered in CSV
        #category_id = response.url.split("categoryId=")[-1]
        if current_page < max_pages:
            next_page = current_page + 1
            next_url = f"https://www.trustpilot.com/_next/data/categoriespages-consumersite-2.718.0/categories/{self.category_id}.json?page={next_page}&categoryId={self.category_id}"
            yield scrapy.Request(url=next_url, callback=self.parse_page,meta={'main_category': main_category, 'sub_category': sub_category})

    