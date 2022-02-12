import scrapy

from scraping_proj.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com"]

    def start_requests(self):
        for url in self.start_urls:
            # If a tag is provided, then only scrape quotes with the
            # specific tag.
            if tag := getattr(self, "tag", None):
                url = f"{url}/tag/{tag}"
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # // means to search in the scope of the whole document.
        # @class in square brackets means to select by class name of
        # the HTML element.
        for quote_selector in response.xpath('//div[@class="quote"]'):
            # ./ means to search in the context of the current selector.
            # text() means to select the text of the HTML element.
            author = quote_selector.xpath(
                './span/small[@class="author"]/text()'
            ).get()
            quote = quote_selector.xpath('./span[@class="text"]/text()').get()
            # Remove the special quotes.
            quote = quote.replace("“", "").replace("”", "")
            tags = quote_selector.xpath(
                './div[@class="tags"]/a[@class="tag"]/text()'
            ).getall()

            quote_item = QuoteItem(author=author, quote=quote, tags=tags)
            yield quote_item

        if next_page_url := response.xpath(
            '//li[@class="next"]/a/@href'
        ).get():
            # With response.follow() we can scrape the next page with
            # the same parse function, recursively.
            yield response.follow(next_page_url, self.parse)
