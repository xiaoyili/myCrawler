from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from dealbot.items import Website


class DealmoonSpider(BaseSpider):
    name = 'dealmoon'
    allowed_domains = ["dealmoon.com"]
    start_urls = [
        "http://dealmoon.com/Computers",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        hxs = HtmlXPathSelector(response)
        li_sites = hxs.select('//div[@class="cat_content_right"]/div/ul/li')
        items = []

        for li in li_sites:
            item = Website()
            item['id'] = li.select('./@id').extract()
            item['detail_link'] = li.select('./div[@class="left_img"]/div/h2/a/@href').extract()
            item['img_src_link'] = li.select('./div[@class="left_img"]/div/a/img').extract()

            items.append(item)

        return items

