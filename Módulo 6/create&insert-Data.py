import os
import sqlite3

os.remove('dsaa.db') if os.path.exists('dsaa.db') else None

conn = sqlite3.connect('dsaa.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS produtos(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT, prod_name TEXT, valor REAL)')
    
def data_insert():
    c.execute('INSERT INTO produtos VALUES(10, "2018-05-02 14:32:11", "Teclado", 90)')
    conn.commit()
    

create_table()
data_insert()
 