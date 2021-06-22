# Scrapy settings for amazonUrlProductListSpider project


BOT_NAME = 'amazonUrlProductListSpider'

SPIDER_MODULES = ['src.spiders']
NEWSPIDER_MODULE = 'src.spiders'
RANDOM_UA_PER_PROXY = True
FAKEUSERAGENT_FALLBACK = 'Mozilla'

POSTGRES_DATABASE = {
    'drivername': 'postgresql+psycopg2',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'postgres',
    'database': 'meisterAffiliateScrapedProducts'
}


# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 600,
    # 'amazonUrlProductListSpider.middlewares.AmazonUrlProductListSpiderDownloaderMiddleware': 543,
    'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 410,
    'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 420,
}


ITEM_PIPELINES = {
    # 'amazonUrlProductListSpider.pipelines.PostgresPipeline': 300,
    # 'amazonUrlProductListSpider.pipelines.DuplicatesPipeline': 400,
    'src.pipelines.CSVPipeline': 400,

                  }
