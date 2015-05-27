# -*- coding: utf-8 -*-
from scrapy.settings.default_settings import DOWNLOAD_DELAY, DOWNLOAD_TIMEOUT,\
    RANDOMIZE_DOWNLOAD_DELAY


# Scrapy settings for news163 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'news163'

SPIDER_MODULES = ['news163.spiders']
NEWSPIDER_MODULE = 'news163.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'news163 (+http://www.yourdomain.com)'
DOWNLOAD_DELAY=1.5
DOWNLOAD_TIMEOUT=100
RANDOMIZE_DOWNLOAD_DELAY=False    #严格按照DOWNLOAD_DELAY来算延时
