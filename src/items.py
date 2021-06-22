# Define here the models for your scraped items
import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


def remove_whitespace(value):
    return value.strip().replace('\n', ' ')


def datetime(value):
    return value.replace('/', '-')


def slugify(value):
    return value.replace(' ', '-').replace(',', '') \
        .replace('(', '').replace(')', '').replace(':', '') \
        .replace('/', '-').replace('®', '')\
        .replace('"', '').replace('|', '')\
        .replace('ü', 'ue').replace('ä', 'ae')\
        .replace('%', '').replace('---', '-')\
        .replace(';', '').replace(' ', '')\
        .replace('™', '').replace('.', '')\
        .replace('+', '').replace('--', '-')\
        .replace('\'', '-').lower()


def clean_price(value):
    return value.replace('\xa0', ' ').replace('€', '').replace(',', '.')


def truncate(value):
    return value[0:69]


def clean_description(value):
    return value.replace('This fits your .', '').replace('Make sure this fits by entering your model number.', '')\
        .replace('P.when("ReplacementPartsBulletLoader").execute(function(module){ module.initializeDPX(); })', '')\
        .replace('Dieser Artikel passt für Ihre .', '')\
        .replace('Geben Sie Ihr Modell ein, um sicherzustellen, dass dieser Artikel passt. ', '')


def clean_title(value):
    return value.replace(' ', '')


def clean_popularity(value):
    return value.replace('Sternebewertungen', '').replace('.', '').replace('ratings', '')\
        .replace(',', '').replace('', '')


def clean_brand(value):
    return value.replace('Besuchen Sie den', '').replace('Marke:', '').replace('Visit the', '')\
        .replace('-Store', '').replace('Store', '').replace('Brand:', '')


def replace_shop_at_amazon_w_blank(value):
    return value.replace('Jetzt bei Amazon.de bestellen!', '')


def replace_amazon_w_meisteraffiliate(value):
    return value.replace('Amazon.de ', 'Meisteraffiliateshop.com')\
        .replace('Amazon.de:', 'Meisteraffiliateshop')


class AmazonUrlProductListSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    meta_description = scrapy.Field(
        input_processor=MapCompose(replace_shop_at_amazon_w_blank, replace_amazon_w_meisteraffiliate),
        output_processor=TakeFirst()
    )
    # meta_description_en = scrapy.Field()
    meta_description_de = scrapy.Field(
        input_processor=MapCompose(replace_shop_at_amazon_w_blank, replace_amazon_w_meisteraffiliate),
        output_processor=TakeFirst()
    )
    # keywords = scrapy.Field(
    #     input_processor=MapCompose(remove_tags, remove_whitespace),
    #     output_processor=TakeFirst()
    # )
    # h1_heading = scrapy.Field()
    # h1_heading_en = scrapy.Field()
    # h1_heading_de = scrapy.Field()
    # meta_robots = scrapy.Field()
    # unavailable_after = scrapy.Field()
    title = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace, truncate, clean_title),
        output_processor=TakeFirst()
    )
    # title_en = scrapy.Field()
    title_de = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace),
        output_processor=TakeFirst()
    )
    slug = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace, slugify),
        output_processor=TakeFirst()
    )
    # slug_en = scrapy.Field()
    slug_de = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace, slugify),
        output_processor=TakeFirst()
    )
    description = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace, clean_description),
        output_processor=TakeFirst()
    )
    # description_en = scrapy.Field()
    description_de = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace),
        output_processor=TakeFirst()
    )
    category = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace),
        output_processor=TakeFirst()
    )
    detail_page_url = scrapy.Field(
        input_processor=MapCompose(remove_tags, ),
        output_processor=TakeFirst()
    )
    # detail_page_url_en = scrapy.Field()
    detail_page_url_de = scrapy.Field()
    asin = scrapy.Field(
        input_processor=MapCompose(remove_tags, ),
        output_processor=TakeFirst()
    )
    uuid = scrapy.Field(

        input_processor=MapCompose(remove_tags, ),
        output_processor=TakeFirst()
    )
    price = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace, clean_price),
        output_processor=TakeFirst()
    )
    availability = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace),
        output_processor=TakeFirst()
    )
    # publisher = scrapy.Field()
    manufacturer = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace, clean_brand),
        output_processor=TakeFirst()
    )
    brand = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace, clean_brand),
        output_processor=TakeFirst()
    )
    publisher = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_whitespace, clean_brand),
        output_processor=TakeFirst()
    )
    medium_image = scrapy.Field(
        input_processor=MapCompose(remove_tags, ),
        output_processor=TakeFirst()
    )
    medium_image_alt = scrapy.Field(
        input_processor=MapCompose(remove_tags, ),
        output_processor=TakeFirst()
    )
    # medium_image_alt_en = scrapy.Field()
    medium_image_alt_de = scrapy.Field(
        input_processor=MapCompose(remove_tags, ),
        output_processor=TakeFirst()
    )
    large_image = scrapy.Field(
        input_processor=MapCompose(remove_tags, ),
        output_processor=TakeFirst()
    )
    large_image_alt = scrapy.Field(
        input_processor=MapCompose(remove_tags, ),
        output_processor=TakeFirst()
    )
    # large_image_alt_en = scrapy.Field()
    large_image_alt_de = scrapy.Field(
        input_processor=MapCompose(remove_tags, ),
        output_processor=TakeFirst()
    )
    popularity = scrapy.Field(
        input_processor=MapCompose(remove_tags, clean_popularity, ),
        output_processor=TakeFirst()
    )
    featured = scrapy.Field()
    created_on = scrapy.Field(
        input_processor=MapCompose(remove_tags, datetime, ),
        output_processor=TakeFirst()
    )
    updated_on = scrapy.Field(
        input_processor=MapCompose(remove_tags, datetime, ),
        output_processor=TakeFirst()
    )

