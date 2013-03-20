# Scrapy settings for dirbot project

SPIDER_MODULES = ['spiders']
NEWSPIDER_MODULE = 'spiders'
DEFAULT_ITEM_CLASS = 'items.Website'

ITEM_PIPELINES = [
    'pipelines.FilterWordsPipeline',
    'pipelines.PricePipeline',
]
