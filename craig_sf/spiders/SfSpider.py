import scrapy
from craig_sf.items import CraigSfItem

class SfSpider(scrapy.Spider):
      name = "sfcraig"
      allowed_domains = ["craigslist.org"]
      start_urls = ["http://sfbay.craigslist.org/search/npo"]

      def parse(sefl,response):
          for sel in response.xpath('//span[@class="pl"]'):
              item = CraigSfItem()
              item['title'] = sel.xpath('a/text()').extract()
              item['link'] = sel.xpath('a/@href').extract()
              yield item
