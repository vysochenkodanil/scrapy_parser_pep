RESULTS_DIR = 'results'

FEED_URI_PARAMS = 'pep_parse.utils.uri_params'

BOT_NAME = "pep_parse"

SPIDER_MODULES = ["pep_parse.spiders"]

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

FEED_EXPORT_ENCODING = "utf-8"

RESULTS_DIR = 'results'
FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}

FEED_STORAGES = {"file": "scrapy.extensions.feedexport.FileFeedStorage"}
