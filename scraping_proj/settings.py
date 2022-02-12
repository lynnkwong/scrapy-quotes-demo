# Reference:
# - https://docs.scrapy.org/en/latest/topics/settings.html

BOT_NAME = "scraping_proj"

SPIDER_MODULES = ["scraping_proj.spiders"]
NEWSPIDER_MODULE = "scraping_proj.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "scraping_proj.pipelines.MongoDBPipeline": 300,
}

# Global settings:
LOG_LEVEL = "INFO"
LOG_FILE = "/tmp/scrapy.log"
LOG_FORMAT = "%(asctime)s : %(levelname)s : %(message)s"

# Spider variables:
MONGO_URI = "mongodb://admin:pass@localhost:27017"
MONGO_DATABASE = "scraping"
MONGO_COLL_QUOTES = "quotes"
