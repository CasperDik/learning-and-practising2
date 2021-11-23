import scrapy
from cmc.cmc.items import CmcItem
from scrapy.crawler import CrawlerProcess

class QuoteSpider(scrapy.Spider):
    name = "crypto"
    start_urls = [
        "https://coinmarketcap.com/"
    ]

    def parse(self, response, **kwargs):
        items = CmcItem()

        name = response.css(".cmc-link .iworPT::text").extract()
        price = response.css(".cLgOOr span::text").extract()
        volume = response.css(".font_weight_500::text").extract()
        marketcap = response.css(".ieFnWP::text").extract()
        circulating_supply = response.css(".kZlTnE::text").extract()

        count = 0
        for _ in name:
            items["name"] = name[count]
            items["price"] = price[count]
            items["volume"] = volume[count]
            items["marketcap"] = marketcap[count]
            items["circulating_supply"] = circulating_supply[count]
            count += 1
            yield items

process = CrawlerProcess(settings={
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'file:///tmp/export.csv'
})

process.crawl(QuoteSpider)
process.start()

