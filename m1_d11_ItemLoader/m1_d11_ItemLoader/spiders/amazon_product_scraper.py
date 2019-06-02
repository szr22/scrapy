import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

from m1_d11_ItemLoader.items import ProductItem

class ProductDetails(scrapy.Spider):
    name  = 'amazon_product_scraper_itemloader'
    start_urls = ['https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=macbook']

    def parse(self, response):

        search_results = response.css('div.s-result-item')
        # print(search_results)

        for product in search_results:
            product_loader = ItemLoader(item=ProductItem(), selector=product)

            # First run without input or output processor defined
            # Then run with only default_input_processor to see that title is getting truncated
            # Then add TakeFirst as the default_output_processor to see that item field values are not arrays any more
            product_loader.default_input_processor = MapCompose(truncate_text)
            product_loader.default_output_processor = TakeFirst()

            product_loader.add_css('title', 'h2.s-line-clamp-2 > a.a-text-normal > span.a-text-normal::text')
            product_loader.add_css('link', 'h2.s-line-clamp-2 > a.a-text-normal::attr(href)')
            product_loader.add_css('price', 'span.a-price > span.a-offscreen::text')
            
            yield product_loader.load_item()

def truncate_text(text):
    return text[:50]