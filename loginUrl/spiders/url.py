import scrapy
import time
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request


#scrapy crawl food -o ingredient.json

class foodSpider(scrapy.Spider):
    name = "url"
    login_url = "https://github.com/login"
    start_urls = ["https://github.com/login"]

    def parse(self, response):
        token = response.css('input[name="authenticity_token"]::attr(value)').extract_first()

        print token        

        data = {
            'csrf_token' : token,
            'login' : 'rvalde28',
            'password' : 'R221487v'
        }

        yield scrapy.FormRequest(url = self.login_url, formdata=data, callback=self.parse_quotes, dont_filter=True);
      
        yield None

    def parse_quotes(self,response):
        print "\n\n\n\n\n\n"
        print response.url
        print "\n\n\n\n\n\n"
        yield None


