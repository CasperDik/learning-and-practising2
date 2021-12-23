import scrapy
from scrapy.crawler import CrawlerProcess
import pandas as pd
from datetime import datetime
from pathlib import Path

class QuoteSpider(scrapy.Spider):
    name = "crypto"
    start_urls = [
        "https://coinmarketcap.com/"
    ]

    def parse(self, response, **kwargs):
        df = pd.DataFrame(columns=["name", "price", "volume", "market cap", "circulating supply"])

        df["name"] = response.css(".cmc-link .iworPT::text").extract()
        df["price"] = response.css(".cLgOOr span::text").extract()
        df["volume"] = response.css(".font_weight_500::text").extract()
        df["market cap"] = response.css(".ieFnWP::text").extract()
        df["circulating supply"] = response.css(".kZlTnE::text").extract()

        downloads_path = str(Path.home() / "Downloads")
        date = str(datetime.today().strftime('%d-%m-%Y_%H%M%S'))
        yield df.to_csv(downloads_path + "\cmc_data_" + date + ".csv", index=False)

process = CrawlerProcess()
process.crawl(QuoteSpider)
process.start()


# todo: make gui & ask for input --> filename, directory to store
# todo: or just make messagebox with where the file is stored
