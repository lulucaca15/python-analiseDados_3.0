import os
from sqlite3.dbapi2 import SQLITE_CREATE_TABLE, SQLITE_INSERT, SQLITE_SELECT 

os.remove("escola.db") if os.path.exists("escola.db") else None

import sqlite3

con = sqlite3.connect("escola.db")
#print(type(con))

cur = con.cursor()
#print(type(cur))

SQLITE_CREATE_TABLE = "CREATE TABLE cursos \
             (id integer primary key, titulo varchar(100), categoria varchar(140))"

cur.execute(SQLITE_CREATE_TABLE)

SQLITE_INSERT = "insert into cursos values (?, ?, ?)"

recset = [
    (1000, "Ciência de Dados", "Data Science"),
    (1001, "Big Data Fundamentos", "Big Data"),
    (1002, "Python Fundamentos", "Análise de Dados")
]

for rec in recset:
    cur.execute(SQLITE_INSERT, rec)

con.commit;

SQLITE_SELECT = "select * from cursos"

cur.execute(SQLITE_SELECT)
dados = cur.fetchall()

for linha in dados:
    print("Curso Id: %d, Titulo: %s, Categoria: %s \n" %linha)

recset = [
    (1003, "Gestão de Dados com MongoDB", "Big Data"),
    (1004, "R Fundamentos", "Analise de Dados")
]

for rec in recset:
    cur.execute(SQLITE_INSERT, rec)

con.commit()    

cur.execute("select * from cursos")

recset = cur.fetchall()

for rec in recset:
    print("Curso Id: %d, Titulo: %s, Categoria: %s \n" %rec)

con.close()


