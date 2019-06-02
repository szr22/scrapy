import scrapy
from m1_d10_Items.items import ProductItem

USDCNY = 6.80

class ProductDetails(scrapy.Spider):
    name  = 'amazon_product_scraper'

    start_urls = ['https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=macbook']

    def parse(self, response):

        search_results = response.css('div.s-result-item')
        # print(search_results)

        for product in search_results:
            
            title = product.css('h2.s-line-clamp-2 > a.a-text-normal > span.a-text-normal::text').extract_first()
            link = product.css('h2.s-line-clamp-2 > a.a-text-normal::attr(href)').extract_first()
            price = product.css('span.a-price>span.a-offscreen::text').extract_first()
            # print(title)
            # print(link)
            # print(price)

            # 
            truncated_title = title

            product_id = link.split('/')[-1]

            short_link = 'https://amazon.com/dp/' + product_id

            cny_price = round(float(price[1:].replace(',', '')) / USDCNY, 2)
            # print(cny_price)
           
            productItem = ProductItem()

            productItem['title'] = truncated_title
            productItem['link'] = short_link
            productItem['price'] = cny_price
            
            # print('\nProduct title: ', productItem['title'])
            # print('Product link: ', productItem['link'])
            # print('Product price: ', productItem['price'], '\n')

            yield productItem
