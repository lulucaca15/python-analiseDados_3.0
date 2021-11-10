import random
import sqlite3
import datetime
import time

conn = sqlite3.connect('dsaa.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, prod_name TEXT, valor REAL)')
    
def data_insert():
    c.execute('INSERT INTO produtos VALUES(10, "2018-05-02 14:32:11", "Teclado", 90)')
    conn.commit()

def data_insert_var():
    new_date = datetime.datetime.now()
    new_prod_name = 'Monitor'
    new_valor = random.randrange(50,100)
    c.execute("INSERT INTO produtos (date, prod_name, valor) VALUES (?, ?, ?)", (new_date, new_prod_name, new_valor))
    conn.commit()
    
for i in range(10):
    data_insert_var()
    time.sleep(1)
    
c.execute('INSERT INTO produtos VALUES(68945, "2018-05-02 14:32:11", "Monitor", 100)')
conn.commit()

c.close()
conn.close()