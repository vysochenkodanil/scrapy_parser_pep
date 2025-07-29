import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        pep = response.css(
            'table.pep-zero-table tbody td a::attr(href)').getall()

        for link in pep:
            link = response.response.urljoin(link)
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
