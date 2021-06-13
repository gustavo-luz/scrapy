# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class ScrapequotesPipeline(object):
    # passando o que ta no database pra POO
    #o init é o fluxo do q vai rodar
    def __init__(self):
        self.create_connection()
        self.create_table()
        pass

    def create_connection(self):
        self.conn = sqlite3.connect("sqlitemyquotes.db")
        self.curr = self.conn.cursor()
    
    def create_table(self):
        # create only if table dont exists
        self.curr.execute("""DROP TABLE IF EXISTS sqlitequotes_table""")
        self.curr.execute("""create table sqlitequotes_table( title text,author text, tag text)""")


    def process_item(self, item, spider):
        self.store_db(item)
        print("pipeline :"+item['title'][0]+item['author'][0])
        return item

    def store_db(self,item):
        #pega os conteúdos do scraper que estavam no yield
        self.curr.execute("""insert into sqlitequotes_table values(?,?,? )""",(
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.conn.commit()
    #commit a conexão
  
    #não vai fechar porque vai estar ligado com o for loop do quotes_spider