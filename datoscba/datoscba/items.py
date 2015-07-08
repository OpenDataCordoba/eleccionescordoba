# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GobItem(scrapy.Item):
    mesa = scrapy.Field()
    A540 = scrapy.Field()
    A500 = scrapy.Field()
    A520 = scrapy.Field()
    P13 = scrapy.Field()
    A590 = scrapy.Field()
    A560 = scrapy.Field()
    A570 = scrapy.Field()
    blancos = scrapy.Field()
    nulos = scrapy.Field()
    recurridos = scrapy.Field()
    impugnados = scrapy.Field()
    total = scrapy.Field()
