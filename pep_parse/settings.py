from pathlib import Path


BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

BASE_DIR = Path(__file__).parent.parent

RESULTS_DIR = 'results'
NAME = "pep"
ALLOWED_HOST = "peps.python.org"
START_URL = "https://peps.python.org/"
FEEDS = {
    f'{RESULTS_DIR}/pep_%(time)s.csv':
    {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True,
    }
}
