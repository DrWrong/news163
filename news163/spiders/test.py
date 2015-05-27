# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from news163.items import News163Item
from bs4 import BeautifulSoup
from news163_django.models import News
from django.core.exceptions import ObjectDoesNotExist
import re


class TestSpider(CrawlSpider):
    name = "test"
    allowed_domains = ["163.com"]
    start_urls = [
        'http://news.163.com/',
        'http://news.163.com/15/0519/17/AQ0D82EC00014JB5.html',
    ]
    rules = [
        Rule(
            LinkExtractor(
                allow=(r'http://news.163.com/15/\d{4}/\d{2}/\w+.html')),
            callback='parse_item', follow=True,),
    ]

    def parse_item(self, response):
        print "here i am running"
        match = re.match(
            r'http://news.163.com/15/\d{4}/\d{2}/(\w+).html', response.url)
        # item["netease_reference_id"] = match.groups()[0]
        netease_reference_id = match.groups()[0]
        try:
            news = News.objects.get(
                netease_reference_id=netease_reference_id)
        except ObjectDoesNotExist:
            item = self.create_news_item_from_beautifysoup(
                BeautifulSoup(response.body))
            item["netease_reference_id"] = netease_reference_id
            item['netease_link'] = response.url
            news = item.save()
            yield item

        for url in news.comment_yield_urls():
            request = scrapy.Request(url, callback=self.parse_comment)
            yield request





    def create_news_item_from_beautifysoup(self, soup):
        item = News163Item()
        item["title"] = soup.find("h1", id="h1title").text.strip()
        source_link = soup.find("a", id="ne_article_source")
        item["source"] = source_link.text.strip()
        item["sourcelink"] = source_link.attrs["source_link"]
        item['content'] = soup.find("div", id="endText").text.strip()
        scripts = soup.find(id="epContentLeft").find_all("script")
        match = re.search(r'tieChannel = "(\w+)"', scripts[5].text)
        item['tieChannel'] = match.groups()[0]
        match = re.search(
            r'threadId = "(?P<thread_id>\w+)",\s+boardId = "(?P<board_id>\w+)"',
            scripts[7].text
        )
        item.update(match.groupdict())
        return item

        # s1 = response.xpath(
        #     '//*[@id="epContentLeft"]/div[10]/script[3]/text()').extract()
        # s2 = s1[0].split('"')
        # item['news_threadId'] = s2[7]
        # item['news_boardId'] = s2[9]
        # s1 = response.xpath(
        #     '//*[@id="epContentLeft"]/div[10]/script[1]/text()').extract()
        # s2 = s1[0].split('"')
        # item['news_tieChannel'] = s2[1]
        # for sel in response.xpath():  # delete? sel.xpath -> response.xpath?
        #     item['article_link'] = response.url.strip()
        #     item['article_title'] = sel.xpath(
        #         '//h1/text()').extract()  # encoude?
        #     item['article_content'] = sel.xpath(
        #         '//div[@id="endText"]/p/text()').extract()
        #     item['article_time'] = sel.xpath(
        #         '//div[@class="ep-time-soure cDGray"]/text()').extract()
        #     item['article_source'] = sel.xpath(
        #         '//div[@class="ep-time-soure cDGray"]/a[@id="ne_article_source"]/text()').extract()
        #     item['article_sourcelink'] = sel.xpath(
        #         '//div[@class="ep-time-soure cDGray"]/a/@href').extract()
        #     item['article_commentlink'] = "http://comment."+item['news_tieChannel'] + \
        #         ".163.com/"+item['news_boardId']+"/" + \
        #         item['news_threadId']+".html"  # item?" "?

        #     print item
        # yield item

        # for page_num in range(1,50,1)
        #     request=scrapy.Request("http://comment."+item['news_tieChannel']+".163.com/cache/newlist/"+item['news_boardId']+"/"+item['news_threadId']+"_"+i+".html",
        #                             callback=self.page_content)
        #     request.meta['item']=item  #passing data
        #     if response.status!=200:
        #         break
        # return request

    # def page_content(self, response):
    #     self.log("content from %s" % response.url)
    #     s = response.body.decode(response.encoding)  # utf-8 -> Unicode
    #     s = s.split('"')
    #     for i in range(0, , 66)
    #         mysql_comment = s[i+15]  # fake code!
    #         mysql_nickname = s[i+23]
    #         mysql_releasetime = s[i+51]
    #         if s[i+15] == s[-64] & &s[i+23] == s[-56] & &s[i+51] == s[-28]:
    #             break

    #     return item  # delete?
