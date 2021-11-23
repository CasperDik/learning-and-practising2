from cmc_scraper import QuoteSpider
from scrapy.crawler import CrawlerProcess

process = CrawlerProcess(settings={
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'cmc.csv'
})

process.crawl(QuoteSpider)
process.start()
