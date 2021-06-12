# scrapy
Repository to practice scrapy at python

<br> <img src="https://img.shields.io/badge/-in%20development-yellow" alt="In development">

## scrapeamazon

* Scraper to scrape amazon products

## scrapequotes

* Scraper to scrape https://quotes.toscrape.com/

### Installing
* move to file location from git

### Creating scrape project
* sudo apt install python3-scrapy
* scrapy startproject [project-name]

### running

* virtualenv venv
    * source venv/bin/activate
    * deactivate

cd [project-name]
scrapy crawl [name-inside-class]
scrapy shell "http://quotes.toscrape.com/" ([url])

[https://www.youtube.com/watch?v=2osL98z3w-Q&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=6](https://www.youtube.com/watch?v=2osL98z3w-Q&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=6)

scrapy

- scrapeamazon (project name)
    - spiders

        init

    - settings.py: nome do bot, modulos que pode colocar, user agent (falar quem vc é, pode bypassar depois)
        - robots.txt (leis da internet pra fazer scraping em um site, por ex ver [https://www.amazon.com/robots.txt](https://www.amazon.com/robots.txt), no entanto, no settings você pode colocar pro seu scraper seguir essas regras)
        - concurrent_requests: máximos requests feitos ao mesmo tempo, cuidado ao colocar muito alto pq causa muitos pedidos e pode deixar mais lento ou fazer cair)
        - AutoThrottle, pra cuidar do overload tambem
    - items.py: coloca os campos

    ![projeto%20scrapy%203308a06619854a099b905d96feec0d83/Untitled.png](projeto%20scrapy%203308a06619854a099b905d96feec0d83/Untitled.png)

    - pipelines: depois de fazer o scraping, tem que store no json, sql, mongodb, esse pipeline faz isso, o que vai na pipeline vai ser gerenciado por ele
    - middleware: cuida do q é adicionado a requisição, ex proxies no request, cuida da request e da resposta do website, fica no meio do scraping e do pipeline

    [passos básico scraper](projeto%20scrapy%203308a06619854a099b905d96feec0d83/passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed.md)