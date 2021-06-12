# passos básico scraper

ver o codigo fonte da pagina

- criar arquivo python na pasta spiders e colocar classe, method de extração
- cria um dicionario com chave valor do que ta extraindo

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled.png)

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%201.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%201.png)

vai pra pasta do projeto scapy e roda o nome criado na classe 

```bash
cd scrapequotes
scrapy crawl quotes
```

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%202.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%202.png)

não deu certo, mudei pra só http e deu

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%203.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%203.png)

pra pegar só o texto

```python
def parse(self, response):
        title = response.css('title::text').extract()
        # mostra como um dicionário
        # yield é como um return, mas ela é usada com gerador que é usado pelo scrapy behind the scenes
        yield {'titletext':title}
        #return super().parse(response)
```

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%204.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%204.png)

## seletor css

```bash
scrapy shell "http://quotes.toscrape.com/"
```

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%205.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%205.png)

pra pegar o titulo tambem

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%206.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%206.png)

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%207.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%207.png)

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%208.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%208.png)

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%209.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%209.png)

ou, pra pegar o indice 0 da página

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2010.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2010.png)

se quiser a quote

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2011.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2011.png)

class: .

id: #

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2012.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2012.png)

pra pegar tudo

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2013.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2013.png)

usar o selector gadget, extensão

[https://chrome.google.com/webstore/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb?hl=pt-BR](https://chrome.google.com/webstore/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb?hl=pt-BR)

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2014.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2014.png)

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2015.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2015.png)

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2016.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2016.png)

# com xpath

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2017.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2017.png)

ex

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2018.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2018.png)

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2019.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2019.png)

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2020.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2020.png)

pegar a classe:

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2021.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2021.png)

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2022.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2022.png)

### combinando

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2023.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2023.png)

selectionar a classe li e a tag a

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2024.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2024.png)

se quiser todas as tags href, todos os links que a pagina pega

![passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2025.png](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/Untitled%2025.png)

[code shell](passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed/code%20shell%20d6388e7ad2884f019d85872b9797dcc4.md)