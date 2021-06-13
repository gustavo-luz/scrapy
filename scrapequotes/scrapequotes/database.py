import sqlite3

#CONECTA, EXECUTA E FECHA
conn = sqlite3.connect('sqlitemyquotes.db')
#cursor variable
curr = conn.cursor()
# add a table
#comment after created
#curr.execute("""create table sqlitequotes_table( title text,author text, tag text)""")
#coloca os values na table
curr.execute("""insert into sqlitequotes_table values('Python with sqlite3','learning scrapy','tagtest' )""")

conn.commit()
conn.close()