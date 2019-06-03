# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MacbookCheck(object):
    def process_item(self, item, spider):
        if ('macbook' not in item['title'].lower() or float(item['price']) < 2000.0):
            item['title'] = 'Non-Macbook'
        return item

class PriceCheck(object):
    def process_item(self, item, spider):
        if float(item['price']) > 15000.0:
            item['price'] = 'Unaffordable'
        return item

class MarkAsViable(object):
    def process_item(self, item, spider):
        if item['title'] != 'Non-Macbook' and item['price'] != 'Unaffordable':
            print('\n\n OPTION FOUND!!')
            print('Link: ', item['link'])
            print('Price: ', item['price'])
            print('Title: ', item['title'], '\n')
        return item