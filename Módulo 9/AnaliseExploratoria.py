#Será usada uma pesquisa nos EIA sobre o mercado de trabalho para programadores de software. 
#O objetivo é fazer uma investigação inicial dos dados a fim de detectar problemas com os dados,
#necessidade de mais variáveis, falhas na organização e necessidades de transformação


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import colorsys
plt.style.use('seaborn-talk')
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('Dados-Pesquisa.csv', sep = ',', low_memory=False)
print(df.head())
print(df)
print(df.describe())


#Distrubuição de Idade
df.Age.hist(bins = 60) 
plt.xlabel("Idade")
plt.ylabel("Numero de Profissionais")
plt.title("Distribuição de Idade")
plt.show()

#Resultado: A maioria dos profissionais que trabalham como programadores de software, estão na faixa
#de idade entre 20 e 30 anos, sendo 25 anos a idade mais frequente.

###################################################

#Distribuição de Sexo

#Definindo quantidade
labels = df.Gender.value_counts().index
num = len(df.EmploymentField.value_counts().index)

#Criando lista de cores
listaHSV = [(x*0.1/num, 0.5, 0.5) for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']

#Gráfico de Pizza
fatias, texto = plt.pie(df.Gender.value_counts(), colors = colors, startangle = 90)
plt.axis('equal')
plt.legend(fatias, labels, bbox_to_anchor = (1.05,1))
plt.title('Sexo')
plt.show()

#Resultado: A grande maioria dos programadores são do sexo masculino

###################################################

#Distribuição de interesses

#Definindo quantidade
num = len(df.JobRoleInterest.value_counts().index)

#Criando lista de cores
listaHSV = [(x*0.1/num, 0.5, 0.5) for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))
labels = df.JobRoleInterest.value_counts().index
colors = ['Green', 'Orange', 'OrangeRed', 'DarkCyan', 'Salmon', 'Sienna', 'Maroon', 'LightSlateGrey', 'DimGray']

#Gráfico de Pizza
fatias, texto = plt.pie(df.JobRoleInterest.value_counts(), colors = colors, startangle = 90)
plt.axis('equal')
plt.legend(fatias, labels, bbox_to_anchor = (0.8,0.7))
plt.title('Interesse Profissional')
plt.show()

#Resultado: A maior parte dos interesses estão voltando para o desenvolvimento web, sendo fullstack o com 
#maior %

###################################################

#Distribuição de EMpregabilidade

num = len(df.EmploymentField.value_counts().index)

listaHSV = [(x*0.1/num, 0.5, 0.5) for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))
labels = df.EmploymentField.value_counts().index
colors = ['Green', 'Orange', 'OrangeRed', 'DarkCyan', 'Salmon', 'Sienna', 'Maroon', 'LightSlateGrey', 'DimGray',
          'red', 'purple', 'pink', 'blue', 'silver']

# Gráfico de Pizza
fatias, texto = plt.pie(df.EmploymentField.value_counts(), colors = colors, startangle = 90)
plt.axis('equal')
plt.legend(fatias, labels, bbox_to_anchor = (0.8,1))
plt.title('Área de Trabalho Atual')
plt.show()

#Resultado: A maioria esmagadora está trabalhando na área de desenvolvimento de software e ti, seguido por educação

###################################################

#Preferência de Trabalho por Idade

#Agrupando os dados
df_ageranges = df.copy()
bins = [0, 20, 30, 40, 50, 60, 100]

df_ageranges["AgeRanges"] = pd.cut(df_ageranges["Age"], bins, labels=["< 20", "20-30", "30-40", "40-50", "50-60", "< 60"])
df2 = pd.crosstab(df_ageranges.AgeRanges, df_ageranges.JobPref).apply(lambda r: r/r.sum(), axis=1)

num = len(df_ageranges.AgeRanges.value_counts().index)

listaHSV = [(x*0.1/num, 0.5, 0.5) for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))

# Gráfico de Barras
ax1 = df2.plot(kind = "bar", stacked = True, color = listaRGB, title = "Preferência de Trabalho por Idade")
lines, labels = ax1.get_legend_handles_labels()
ax1.legend(lines, labels, bbox_to_anchor = (1.51, 1))

help(pd.crosstab)

###################################################

#Realocação por Idade

df3 = pd.crosstab(df_ageranges.AgeRanges, df_ageranges.JobRelocateYesNo).apply(lambda r: r/r.sum(), axis=1)

num = len(df_ageranges.AgeRanges.value_counts().index)

listaHSV = [(x*0.1/num, 0.5, 0.5) for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))

#Gráfico de Barras
ax1 = df2.plot(kind = "bar", stacked = True, color = listaRGB, title = "Realocação por Idade")
lines, labels = ax1.get_legend_handles_labels()
ax1.legend(lines, ["Não", "Sim"], loc = 'best')

###################################################

#Idade x Horas de Aprendizagem

#Criando subset dos dados
df9 = df.copy()
df9 = df9.dropna(subset=['HoursLearning'])
df9 = df9[df['Age'].isin(range(0,70))]

#Definindo valores de X e Y

x = df9.Age
y = df9.HoursLearning

#Computando os valores e gerando grafico

m, b = np.polyfit(x, y, 1)
plt.plot(x, y, '.')
plt.plot(x, m*x + b, '-', color = 'red')
plt.xlabel("Idade")
plt.ylabel("Horas de Treinamento")
plt.title("Idade por Horas de Treinamento")
plt.show()


###################################################

#Investimento em Capacitação x Expectativa Salarial

df5 = df.copy()
df5 = df5.dropna(subset=["ExpectedEarning"])
df5 = df5[df['MoneyForLearning'].isin(range(0,60000))]

x = df5.MoneyForLearning
y = df5.ExpectedEarning

m, b = np.polyfit(x, y, 1)
plt.plot(x, y, '.')
plt.plot(x, m*x + b, '-', color = 'red')
plt.xlabel("Investimento em Treinamento")
plt.ylabel("Expectativa Salarial")
plt.title("Investimento em Treinamento vs Expectativa Salarial")
plt.show()
