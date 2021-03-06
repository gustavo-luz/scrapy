import scrapy
from ..items import ScrapequotesItem


# classe que vai herdar das classes criadas
class QuoteSpider (scrapy.Spider):
    name = 'quotes'
    #lista dos sites que quer fazer o scrapy
    #main page
    start_urls = ['http://quotes.toscrape.com/']
   
   

    # quer so o título do site
    #o response tem o codigo fonte do site, é de lá que se extrai
    def parse(self, response):
        #retornar a primeira observação de cada
        items = ScrapequotesItem()

        all_div_quotes = response.css('div.quote')
        #1 quote por 1
        for quotes in all_div_quotes:

            title = quotes.css('span.text::text').extract()
            #extract the span
            #extract the author
            author = quotes.css('.author::text').extract()
            #tags: pega so a classe tags
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag    
            # mostra como um dicionário
            # yield é como um return, mas ela é usada com gerador que é usado pelo scrapy behind the scenes
            yield items
        #class li, dentro dela pega o atributo de href que é o link

        
        next_page = response.css('li.next a::attr(href)').get()
         # encontrar o botao, o link, ir pro link ate que apareçam novas paginas
        if next_page is not None: #se não tiver o botão next na página em questão
            yield response.follow(next_page,callback=self.parse)
            #metodo do scrapy em que se coloca a página e depois continua fazendo o parse até acabar, função recursiva 
        