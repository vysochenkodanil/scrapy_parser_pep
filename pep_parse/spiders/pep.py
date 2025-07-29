import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        all_links = response.css('a[href^="pep-"]')
        if (
            response.url == self.start_urls[0] and len(all_links) != 0
        ):
            for link in all_links:
                yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_number = response.css("h1.page-title::text").get().split()[1]
        pep_name = response.css(
            "h1.page-title::text").get()
        pep_status = response.css(
            'dt:contains("Status") + dd::text').get() or "Unknown"

        yield PepParseItem(number=pep_number, name=pep_name, status=pep_status)
