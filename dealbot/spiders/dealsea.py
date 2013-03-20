from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from dealbot.items import Website


class DealseaSpider(BaseSpider):
    name = 'dealsea'
    allowed_domains = ["dealsea.com"]
    start_urls = [
        "http://dealsea.com/",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul[@class="directory-url"]/li')
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.select('a/text()').extract()
            item['url'] = site.select('a/@href').extract()
            item['description'] = site.select('text()').extract()
            items.append(item)

        return items

