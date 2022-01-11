import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as pl
import seaborn as sea

dados = sea.load_dataset('tips')
print(dados.head())

sea.jointplot('total_bill', 'tip', data = dados, kind='reg')

sea.lmplot('total_bill', 'tip', data = dados, col = 'smoker')

# df = pd.DataFrame()
# df['a'] = random.sample(range(1, 100), 25)
# df['b'] = random.sample(range(1, 100), 25)
# print(df.head())
