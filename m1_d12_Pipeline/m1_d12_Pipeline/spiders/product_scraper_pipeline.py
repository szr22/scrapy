import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from m1_d12_Pipeline.items import ProductItem


class ProductDetails(scrapy.Spider):
    name  = 'product_scraper_pipeline'

    start_urls = ['https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=macbook']

    def parse(self, response):

        search_results = response.css('div.s-result-item')

        for product in search_results:

            product_loader = ItemLoader(item=ProductItem(), selector=product)

            product_loader.default_output_processor = TakeFirst()

            product_loader.add_css('title', 'h2.s-line-clamp-2 > a.a-text-normal > span.a-text-normal::text')
            product_loader.add_css('link', 'h2.s-line-clamp-2 > a.a-text-normal::attr(href)')
            product_loader.add_css('price', 'span.a-price > span.a-offscreen::text')

            print('\n')
            
            yield product_loader.load_item()