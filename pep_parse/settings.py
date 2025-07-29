from datetime import datetime
from pathlib import Path

RESULTS_DIR = Path("results")

RESULTS_DIR.mkdir(exist_ok=True)

BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    "results/pep_%(time)s.csv": {
        "format": "csv",
        "fields": ["number", "name", "status"],
        "overwrite": True,
    }
}

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}

FEED_STORAGES = {"file": "scrapy.extensions.feedexport.FileFeedStorage"}
