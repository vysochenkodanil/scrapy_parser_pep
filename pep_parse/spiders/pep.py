import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import NAME, ALLOWED_HOST, START_URL


class PepSpider(scrapy.Spider):
    name = NAME
    allowed_domains = [ALLOWED_HOST]
    start_urls = [START_URL]

    def parse(self, response):
        pep = response.css(
            'table.pep-zero-table tbody td a::attr(href)').getall()

        for link in pep:
            link = response.urljoin(link)
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css('.page-title::text').get().split(' – ')
        status = response.css(
            'dt:contains("Status") + dd abbr::text').get(),

        yield PepParseItem(
            number=number,
            name=name,
            status=status
        )
