from datetime import datetime
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.loader import ItemLoader
from src.items import AmazonUrlProductListSpiderItem
import uuid as uuid_lib


class AmazonUrlProductListSpider(scrapy.Spider):
    name = 'amazon_url_product_list_spider'
    allowed_domains = ['amazon.de']
    start_urls = [
        'https://amzn.to/3gptKVr',
        'https://amzn.to/2TCCKOc',
        'https://amzn.to/3vsahI8',
        'https://amzn.to/3gFUDDq',
        'https://amzn.to/2RYYpiX',
        'https://amzn.to/3zFPGDw',
        'https://amzn.to/2S5mvsA',
        'https://amzn.to/3wA7kqc',
        'https://amzn.to/3gtuzwH',
        'https://amzn.to/3pWWJmC',
        'https://amzn.to/3gvRUxq',
        'https://amzn.to/2SvEI2M',
        'https://amzn.to/2S5uFkI',
        'https://amzn.to/3gqAano',
        'https://amzn.to/2Tz4SBF',
        'https://amzn.to/3gs14eA',
        'https://amzn.to/3vwkIuf',
        'https://amzn.to/3gu4ygH',
        'https://amzn.to/35q08Rx',
        'https://amzn.to/3gspggF',
        'https://amzn.to/35qVvqq',
        'https://amzn.to/3gu79XZ',
        'https://amzn.to/3gqoscm',
        'https://amzn.to/3gu5hOL',
        'https://amzn.to/3q11xHW',
        'https://amzn.to/35pmqmi',
        'https://amzn.to/3gqWGMW',
        'https://amzn.to/3pZgfyR',
        'https://amzn.to/3gub8Uv',
        'https://amzn.to/35sWhDb',
        'https://amzn.to/3cJpeyO',
        'https://amzn.to/3gsBwhe',
        'https://amzn.to/3q7d1JW',
        'https://amzn.to/3vpqSw4',
        'https://amzn.to/2S14nQp',
        'https://amzn.to/3vtlyrx',
        'https://amzn.to/3wuGEqF',
        'https://amzn.to/3grHkrh',
        'https://amzn.to/3cJE4oU',
    ]

    def parse(self, response):
        x = uuid_lib.uuid4()
        now = datetime.now()
        l = ItemLoader(item=AmazonUrlProductListSpiderItem(), response=response)

        l.add_xpath("meta_description", "//meta[@name='description']/@content")
        # l.add_xpath("keywords", "//meta[@name='keywords']/@content")
        l.add_xpath("title", "//*[@id='productTitle']")
        l.add_xpath("slug", "//*[@id='productTitle']")
        l.add_xpath("description", "//*[@id='feature-bullets']")
        l.add_value("detail_page_url", response.url)
        l.add_xpath("asin", "//*[@id='ASIN']/@value")
        l.add_xpath("medium_image", "//*[@id='landingImage']/@src")
        l.add_xpath("large_image", "//*[@id='landingImage']/@src")
        # l.add_xpath("category", "//*[@id='wayfinding-breadcrumbs_feature_div']/ul/li[3]/span/a")
        # l.add_value("category", "1")
        l.add_value("uuid", str(x))
        l.add_xpath("price", "//span[contains(@id, 'ourprice') or contains(@id, 'saleprice')]")
        # l.add_xpath("availability", "//div[@id='availability']")
        l.add_xpath("brand", "//*[@id='bylineInfo']")
        l.add_xpath("publisher", "//*[@id='bylineInfo']")
        l.add_xpath("manufacturer", "//*[@id='bylineInfo']")
        l.add_xpath("medium_image_alt", "//*[@id='landingImage']/@alt")
        l.add_xpath("large_image_alt", "//*[@id='landingImage']/@alt")
        l.add_xpath("popularity", "//*[@id='acrCustomerReviewText']")
        # l.add_value("featured", 0)
        l.add_value("created_on", now.strftime("%Y/%m/%d %H:%M:%S"))
        l.add_value("updated_on", now.strftime("%Y/%m/%d %H:%M:%S"))

        return l.load_item()


class DE_AmazonUrlProductListSpider(scrapy.Spider):
    name = 'de_amazon_url_product_list_spider'
    allowed_domains = ['amazon.de']
    start_urls = [
        'https://amzn.to/35rhbTe',
        'https://amzn.to/3gtvo8q',
        'https://amzn.to/3grtYLS',
        'https://amzn.to/35qlz50',
        'https://amzn.to/2TF5k1u',
        'https://amzn.to/3grA0Mw',
        'https://amzn.to/3pWxGjy',
        'https://amzn.to/3gEo3lo',
        'https://amzn.to/2S3LTim',
        'https://amzn.to/3wu72Bi',
        'https://amzn.to/3pWWYhH',
        'https://amzn.to/3cL7LWC',
        'https://amzn.to/3grWmNK',
        'https://amzn.to/3vAGhde',
        'https://amzn.to/3iFOA4y',
        'https://amzn.to/2TCf8sK',
        'https://amzn.to/3vwWujr',
        'https://amzn.to/35sEdsR',
        'https://amzn.to/35sIs7K',
        'https://amzn.to/3gsdnaz',
        'https://amzn.to/3gvr8W6',
        'https://amzn.to/3pZICNw',
        'https://amzn.to/3wz5oy4',
        'https://amzn.to/2SwVXke',
        'https://amzn.to/3pWOFCy',
        'https://amzn.to/3wv9DLl',
        'https://amzn.to/3xrHWTs',
        'https://amzn.to/3wvsSUJ',
        'https://amzn.to/3vpj0e0',
        'https://amzn.to/35oIBcD',
        'https://amzn.to/3wvbhwn',
        'https://amzn.to/3xoSCSN',
        'https://amzn.to/3wvzXVj',
        'https://amzn.to/2TyIwAg',
        'https://amzn.to/35rIsVS',
        'https://amzn.to/3zxmG0n',
        'https://amzn.to/35myKUC',
        'https://amzn.to/3grwuSk',
        'https://amzn.to/3cJE4oU',
    ]

    def parse(self, response):
        x = uuid_lib.uuid4()
        now = datetime.now()
        l = ItemLoader(item=AmazonUrlProductListSpiderItem(), response=response)

        l.add_xpath("meta_description_de", "//meta[@name='description']/@content")
        # l.add_xpath("keywords", "//meta[@name='keywords']/@content")
        l.add_xpath("title_de", "//*[@id='productTitle']")
        l.add_xpath("slug_de", "//*[@id='productTitle']")
        l.add_xpath("description_de", "//*[@id='feature-bullets']")
        l.add_value("detail_page_url_de", response.url)
        l.add_xpath("asin", "//*[@id='ASIN']/@value")
        # l.add_xpath("medium_image", "//*[@id='landingImage']/@src")
        # l.add_xpath("large_image", "//*[@id='landingImage']/@src")
        # l.add_xpath("category", "//*[@id='wayfinding-breadcrumbs_feature_div']/ul/li[3]/span/a")
        # l.add_value("category", "1")
        # l.add_value("uuid", str(x))
        # l.add_xpath("price", "//span[contains(@id, 'ourprice') or contains(@id, 'saleprice')]")
        # l.add_xpath("availability", "//div[@id='availability']")
        # l.add_xpath("brand", "//*[@id='bylineInfo']")
        # l.add_xpath("publisher", "//*[@id='bylineInfo']")
        # l.add_xpath("manufacturer", "//*[@id='bylineInfo']")
        l.add_xpath("medium_image_alt_de", "//*[@id='landingImage']/@alt")
        l.add_xpath("large_image_alt_de", "//*[@id='landingImage']/@alt")
        # l.add_xpath("popularity", "//*[@id='acrCustomerReviewText']")
        # l.add_value("featured", 0)
        l.add_value("created_on", now.strftime("%Y/%m/%d %H:%M:%S"))
        l.add_value("updated_on", now.strftime("%Y/%m/%d %H:%M:%S"))

        return l.load_item()