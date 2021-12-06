import pandas as pd
from pandas import Series
from pandas.core.frame import DataFrame


# print(pd.__version__)

# Obj = Series([67,78,-56,13])
# print(Obj)

# print(type(Obj))
# print(Obj.values)
# print(Obj.index)

# Obj2 = Series([67,78,-56,13], index=['a', 'b', 'c', 'd'])
# print(Obj2)
# print(Obj2.values)
# print(Obj2.index)

# print(Obj2[Obj2 > 3])
# print(Obj2['b'])
# print('d' in Obj2)

# dict = {'Futebol': 5200, 'Tenis': 120, 'Natação': 698, 'Volei': 1550}
# Obj3 = Series(dict)
# print(Obj3)
# print(type(Obj3))

# esportes = ['Futebol', 'Tenis', 'Natação', 'Basquete']
# Obj4 = Series(dict, index=esportes)
# print(Obj4)

# print(pd.isnull(Obj4))
# print(pd.notnull(Obj4))

# print(Obj4.isnull())

# print(Obj3+Obj4)

# Obj4.name = 'população'
# Obj4.index.name = 'esporte'
# print(Obj4)

data = {'Estado': ['Santa Catarina', 'Paraná', "Goiás", "Bahia", "Minas Gerais"],
        'Ano' : [2002,2003,2004,2005,2006],
        'População': [1.5,1.7,3.6,2.4,2.9]}

# frame = DataFrame(data)
# print(frame)

# print(type(frame))

# print(DataFrame(data, columns=['Ano', 'Estado', 'População']))

frame2 = DataFrame(data, columns = ['Ano', 'Estado', "População", 'Débito'],
                  index = ['um', 'dois', 'tres', 'quatro', 'cinco'])

print(frame2)

# print(frame2['Estado'])

# print(type(frame2))
# print(frame2.index)
# print(frame2.columns)

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
