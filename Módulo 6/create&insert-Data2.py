import random
import sqlite3
import datetime
import time
import matplotlib.pyplot as plt

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
    
def leitura_todos_dados():
    c.execute("SELECT * FROM PRODUTOS")
    for linha in c.fetchall():
        print(linha)
        
def leitura_registros():
    c.execute("SELECT * FROM PRODUTOS WHERE valor > 60.0")
    for linha in c.fetchall():
        print(linha)
        
def leitura_colunas():
    c.execute("SELECT * FROM PRODUTOS")
    for linha in c.fetchall():
        print(linha[3])
        
def atualiza_dados():
    c.execute("UPDATE produtos SET valor = 70.0 WHERE valor = 82.0")    
    conn.commit()

def remove_dados():
    c.execute("DELETE FROM produtos WHERE valor = 66.0")
    conn.commit()
    
    
def dados_grafico():
    c.execute("SELECT id, valor FROM produtos")
    ids = []
    valores = []
    dados = c.fetchall()
    for linha in dados:
        ids.append(linha[0])
        valores.append(linha[1])
    
    plt.bar(ids, valores)
    plt.show()    
    
#for i in range(10):
#    data_insert_var()
#    time.sleep(1)
    
#conn.commit()

#leitura_todos_dados()
#leitura_registros()
#leitura_colunas()

#leitura_todos_dados()
#atualiza_dados()
#leitura_todos_dados()
#remove_dados()
#leitura_todos_dados()

dados_grafico()

c.close()
conn.close()

