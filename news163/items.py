# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class News163Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    article_commentlink=scrapy.Field()
    article_content=scrapy.Field()
    article_link=scrapy.Field()
    article_source=scrapy.Field()
    article_sourcelink=scrapy.Field()  
    article_time=scrapy.Field()
    article_title=scrapy.Field()
    news_boardId=scrapy.Field()
    news_threadId=scrapy.Field()
    news_tieChannel=scrapy.Field()
        
