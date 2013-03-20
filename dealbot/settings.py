# Scrapy settings for dirbot project

SPIDER_MODULES = ['dealbot.spiders']
NEWSPIDER_MODULE = 'dealbot.spiders'
DEFAULT_ITEM_CLASS = 'dealbot.items.Website'

ITEM_PIPELINES = [
    'dealbot.pipelines.FilterWordsPipeline',
    'dealbot.pipelines.PricePipeline',
]
