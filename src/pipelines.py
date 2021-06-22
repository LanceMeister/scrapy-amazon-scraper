# ---------------POSTGRES-------------------------------#

# from sqlalchemy import create_engine
# from sqlalchemy.engine import URL
# from amazonUrlProductListSpider import settings
# from sqlalchemy.orm import sessionmaker
# from amazonUrlProductListSpider.models import ProductDB, create_table, db_connect


# class PostgresPipeline(object):
#     def __init__(self):
#         """
#         Initializes database connection and sessionmaker.
#         Creates product table.
#         """
#         engine = db_connect()
#         create_table(engine)
#         self.Session = sessionmaker(bind=engine)
#
#     def process_item(self, item, spider):
#         """Save products in the database.
#
#         This method is called for every item pipeline component.
#         """
#         session = self.Session()
#         self.Session.configure(bind=create_engine(URL(**settings.POSTGRES_DATABASE)))
#         product_db = ProductDB(**item)
#
#         try:
#             if session.query(ProductDB).filter_by(asin=item['asin']).first() is None:
#                 session.add(product_db)
#                 session.commit()
#
#         except:
#             session.rollback()
#             raise print('ERROR!!! Some Items May Not Have Been Added!')
#         finally:
#             session.close()
#         return item

# --------------END--POSTGRES--------------------------------#


# --------------CSV------------------------------------------#

from scrapy.exporters import CsvItemExporter
from scrapy import signals


class CSVPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.file = open('output.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

# --------------END--CSV--------------------------------#
