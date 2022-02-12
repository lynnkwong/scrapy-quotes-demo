import scrapy


class QuoteItem(scrapy.Item):
    """Define the Item fields that will be scraped.

    Field() is used to specify the meta data for the Item field, such
    as the serializer. Most of the time we don't need to specify any
    meta data for the Item field.
    """
    author = scrapy.Field()
    quote = scrapy.Field()
    tags = scrapy.Field()
