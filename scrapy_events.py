import scrapy
from scrapy.crawler import CrawlerProcess


class PythonEventsSpider(scrapy.Spider):
    name = 'pythoneventsspider'
    start_urls = ['https://www.python.org/events/python-events/',]
    found_events = []

    def parse(self, response):
        for event in response.xpath('//ul[contains(@class, "list-recent-events")]/li'):
            event_details = dict()
            event_details['name'] = event.xpath('h3[@class="event-title"]/a/text()').get()
            event_details['location'] = event.xpath('p/span[@class="event-location"]/text()').get()
            event_details['time'] = event.xpath('p/time/text()').get()
            self.found_events.append(event_details)
        if __name__ == "__main__":
            process = CrawlerProcess({'LOG_LEVEL': 'ERROR'})
            process.crawl(PythonEventsSpider)
            spider = next(iter(process.crawlers)).spider
            process.start()
            for event in spider.found_events:
                print(event)
#%%
