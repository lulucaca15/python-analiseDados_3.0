import matplotlib
import pandas as pd
from pandas import Series
from pandas.core.frame import DataFrame


print(pd.__version__)

Obj = Series([67,78,-56,13])
print(Obj)

print(type(Obj))
print(Obj.values)
print(Obj.index)

Obj2 = Series([67,78,-56,13], index=['a', 'b', 'c', 'd'])
print(Obj2)
print(Obj2.values)
print(Obj2.index)

print(Obj2[Obj2 > 3])
print(Obj2['b'])
print('d' in Obj2)

dict = {'Futebol': 5200, 'Tenis': 120, 'Natação': 698, 'Volei': 1550}
Obj3 = Series(dict)
print(Obj3)
print(type(Obj3))

esportes = ['Futebol', 'Tenis', 'Natação', 'Basquete']
Obj4 = Series(dict, index=esportes)
print(Obj4)

print(pd.isnull(Obj4))
print(pd.notnull(Obj4))

print(Obj4.isnull())

print(Obj3+Obj4)

Obj4.name = 'população'
Obj4.index.name = 'esporte'
print(Obj4)

data = {'Estado': ['Santa Catarina', 'Paraná', "Goiás", "Bahia", "Minas Gerais"],
        'Ano' : [2002,2003,2004,2005,2006],
        'População': [1.5,1.7,3.6,2.4,2.9]}

frame = DataFrame(data)
print(frame)

print(type(frame))

print(DataFrame(data, columns=['Ano', 'Estado', 'População']))

frame2 = DataFrame(data, columns = ['Ano', 'Estado', "População", 'Débito'],
                  index = ['um', 'dois', 'tres', 'quatro', 'cinco'])

print(frame2)

print(frame2['Estado'])

print(type(frame2))
print(frame2.index)
print(frame2.columns)

import numpy as np

frame2['Débito'] = np.arange(5.)
print(frame2)

print(frame2.values)
print(frame2.describe())

print(frame2['dois' : 'quatro'])
# print(frame2 < 5)

print(frame2.loc['quatro'])
print(frame2.iloc[2])

web_stats= {'Dias': [1,2,3,4,5,6,7],
            'Visitantes': [45,23,67,78,23,12,14],
            'Taxas': [11,22,33,44,55,66,77]
            }

df = pd.DataFrame(web_stats)
print(df)

print(df.set_index('Dias'))
print(df.head())
print(df['Visitantes'])
print(df[['Visitantes', 'Taxas']])

df = pd.read_csv('salarios.csv')
print(df)

df = pd.read_table('salarios.csv', sep = ',')
print(df)

df = pd.read_csv('salarios.csv', names = ['a', 'b', 'c', 'd'])
print(df)

import sys

data = pd.read_csv('salarios.csv')
print(data.to_csv(sys.stdout, sep = '|'))

dates = pd.date_range('20180101', periods = 10)
df = pd.DataFrame(np.random.randn(10,4), index = dates, columns = list('ABCD'))

print(df)
print(df.head())
print(df.describe())
print(df.mean())
print(df.mean(1))
print(df.apply(np.cumsum))

left = pd.DataFrame({'chave': ['chave1', 'chave2'], 'coluna1' : [1,2]})
right = pd.DataFrame({'chave': ['chave1', 'chave2'], 'coluna2' : [3,4]})
print(pd.merge(left,right, on='chave'))

df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
print(df)

s = df.iloc(3)
print(s)

df.append(s, ingnore_index = True)
print(df)

rng = pd.date_range('1/1/2018', periods = 50, freq = 'S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index = rng)

print(ts)

import matplotlib.pyplot as plt
from matplotlib import style

ts = pd.Series(np.random.randn(500), index = pd.date_range('1/1/2016', periods = 500))
ts = ts.cumsum()
ts.plot()
plt.show()

df = pd.DataFrame(np.random.randn(500, 4), index = ts.index, columns = ['A', 'B', 'C', 'D'])
df = df.cumsum()
plt.figure(); df.plot(); plt.legend(loc = 'best')
plt.show()

import os
df.to_excel('teste-df-output.xlsx', sheet_name='Sheet1')

newDf2 = pd.read_excel('teste-df-output.xlsx', 'Sheet1', index_col=None, na_values = ('NA'))
print(newDf2.head())
os.remove('teste-df-output.xlsx')
