import scrapy
# classe que vai herdar das classes criadas
class QuoteSpider (scrapy.Spider):
    name = 'quotes'
    #lista dos sites que quer fazer o scrapy
    start_urls = ['http://quotes.toscrape.com/']

    # quer so o título do site
    #o response tem o codigo fonte do site, é de lá que se extrai
    def parse(self, response):
        title = response.css('title::text').extract()
        # mostra como um dicionário
        # yield é como um return, mas ela é usada com gerador que é usado pelo scrapy behind the scenes
        yield {'titletext':title}
        #return super().parse(response)