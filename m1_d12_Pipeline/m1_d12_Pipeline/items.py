# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose

USDCNY = 6.80

def convert_price(price):
    if price:
        return round(float(price[1:].replace(',', '')) * USDCNY,2)

def shorten_amazon_link(link):
    product_id = link.split('/')[-1]
    return 'https://amazon.com/dp/' + product_id


class ProductItem(scrapy.Item):

    title = scrapy.Field()

    price = scrapy.Field(
    					input_processor = MapCompose(convert_price)
        				)

    link = scrapy.Field(
    					input_processor = MapCompose(shorten_amazon_link)
        				)
