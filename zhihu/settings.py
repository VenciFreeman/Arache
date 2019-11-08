BOT_NAME = 'zhihuspider'

SPIDER_MODULES = ['zhihuspider.spiders']
NEWSPIDER_MODULE = 'zhihuspider.spiders'

ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1

DEFAULT_REQUEST_HEADERS = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}

DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
   'zhihuspider.middlewares.ZhihuspiderDownloadmiddlewareRandomUseragent': 543,
}

ITEM_PIPELINES = {
    'zhihuspider.pipelines.ZhihuspiderPipeline': 300,
}
