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

or cd scrapy
e
scrapy shell "http://quotes.toscrape.com/" ([url])

[https://www.youtube.com/watch?v=2osL98z3w-Q&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=6](https://www.youtube.com/watch?v=2osL98z3w-Q&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=6)

scrapy


- scrapeamazon (project name)
    - spiders

        init

    - settings.py: name of the bot, modules it can place, user agent (say who you are, you can bypass it later)
        - robots.txt (Internet laws for scraping a website, eg see [https://www.amazon.com/robots.txt](https://www.amazon.com/robots.txt), on However, in the settings you can set your scraper to follow these rules)
        - concurrent_requests: maximum requests made at the same time, be careful when setting it too high because it causes many requests and can make it slower or crash)
        - AutoThrottle, to take care of the overload too
    - items.py: put the fields
    
    ![projeto%20scrapy%203308a06619854a099b905d96feec0d83/Untitled.png](projeto%20scrapy%203308a06619854a099b905d96feec0d83/Untitled.png)

   - pipelines: after doing the scraping, you have to store it in json, sql, mongodb, this pipeline does that, what goes in the pipeline will be managed by it
   - middleware: takes care of what is added to the request, ex proxies in the request, takes care of the request and the response from the website, is in the middle of scraping and the pipeline

    [basic steps scraper](projeto%20scrapy%203308a06619854a099b905d96feec0d83/passos%20ba%CC%81sico%20scraper%20b394aa42c65b4e5ab6cebdea33c04bed.md)
