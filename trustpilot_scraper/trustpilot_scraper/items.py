# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TrustpilotScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    main_category = scrapy.Field()
    main_link = scrapy.Field()
    sub_category = scrapy.Field()
    sub_category_link = scrapy.Field()
    pass

class CategoryItem(scrapy.Item):
    main_category = scrapy.Field()
    main_link = scrapy.Field()
    sub_category = scrapy.Field()
    sub_category_id = scrapy.Field()
    sub_category_link = scrapy.Field()


class DataIteam(scrapy.Item):
    main_category =scrapy.Field()
    sub_category = scrapy.Field()
    businessName = scrapy.Field()
    reviewPageName = scrapy.Field()
    stars = scrapy.Field()
    trustScore = scrapy.Field()
    numberOfReviews = scrapy.Field()
    logoUrl = scrapy.Field()
    address = scrapy.Field()
    city = scrapy.Field()
    zipCode = scrapy.Field()
    country = scrapy.Field()
    website = scrapy.Field()
    email = scrapy.Field()
    phone = scrapy.Field()
    category_data = scrapy.Field()