import scrapy
from pep_parse.items import PepParseItem
from urllib.parse import urljoin

class PepSpider(scrapy.Spider):
    name = 'pep'
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        pep_links = response.css('a[href^="pep-"]::attr(href)').getall()
        for link in pep_links:
            yield response.follow(
                urljoin(response.url, link),
                callback=self.parse_pep
            )

    def parse_pep(self, response):
        pep_number = response.css('h1.page-title::text').get().split()[1]
        pep_name = response.css('h1.page-title::text').get()
        pep_status = response.css('dt:contains("Status") + dd::text').get() or 'Unknown'
        
        yield PepParseItem(
            number=pep_number,
            name=pep_name,
            status=pep_status
        )
