from pathlib import Path
from datetime import datetime


RESULTS_DIR = Path('results')
BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

FEED_EXPORT_ENCODING = 'utf-8'

timestamp = datetime.now().strftime("%Y%m%d")

FEEDS = {
    f"results/pep_{timestamp}.csv": {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
    }
}
ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEED_STORAGES = {'file': 'scrapy.extensions.feedexport.FileFeedStorage'}
