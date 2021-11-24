import pandas as pd
import numpy as np

load_file = "dados_compras.json"
purchase_file = pd.read_json(load_file, orient = "records")
purchase_file.head()

player_demographics = purchase_file.loc[:, ["Sexo", "Login", "Idade"]]
player_demographics.head()

player_demographics = player_demographics.drop_duplicates()
player_count = player_demographics.count()[0]
player_count

pd.DataFrame({"Total de Jogadores" : [player_count]})

average_item_price = purchase_file["Valor"].mean()
total_item_price = purchase_file["Valor"].sum()
total_item_count = purchase_file["Valor"].count()
item_id = len(purchase_file["Item ID"].unique())

# Dataframe para os resultados
summary_calculations = pd.DataFrame({"Número de Itens Únicos" : item_id,
                                     "Número de Compras" : total_item_count, 
                                     "Total de Vendas" : total_item_price, 
                                     "Preço Médio" : [average_item_price]})

# Data Munging
summary_calculations = summary_calculations.round(2)
summary_calculations ["Preço Médio"] = summary_calculations["Preço Médio"].map("${:,.2f}".format)
summary_calculations ["Total de Vendas"] = summary_calculations["Total de Vendas"].map("${:,.2f}".format)
summary_calculations = summary_calculations.loc[:, ["Número de Itens Únicos", "Preço Médio", "Número de Compras", "Total de Vendas"]]

summary_calculations

purchase_file["Item ID"].unique()

# Cálculos básicos
gender_count = player_demographics["Sexo"].value_counts()
gender_percent = (gender_count / player_count) * 100

# Dataframe para os resultados
gender_demographics = pd.DataFrame({"Sexo" : gender_count, 
                                    "%" : gender_percent})

# Data Munging
gender_demographics = gender_demographics.round(2)
gender_demographics ["%"] = gender_demographics["%"].map("{:,.1f}%".format)

gender_count
gender_percent
gender_demographics

gender_total_item_price = purchase_file.groupby(["Sexo"]).sum()["Valor"].rename("Total de Vendas")
gender_average_item_price = purchase_file.groupby(["Sexo"]).mean()["Valor"].rename("Average Price")
purchase_count = purchase_file.groupby(["Sexo"]).count()["Valor"].rename("Número de Compras")
normalized_total = gender_total_item_price / gender_demographics["Sexo"]

# Armazenando o resultado em um Dataframe
gender_purchasing_analysis = pd.DataFrame({"Número de Compras" : purchase_count, 
                                           "Valor Médio Por Item" : gender_average_item_price, 
                                           "Total de Vendas" : gender_total_item_price, 
                                           "Total Normalizado" : normalized_total})

# Data Munging
gender_purchasing_analysis = gender_purchasing_analysis.round(2)
gender_purchasing_analysis ["Valor Médio Por Item"] = gender_purchasing_analysis["Valor Médio Por Item"].map("${:,.2f}".format)
gender_purchasing_analysis ["Total de Vendas"] = gender_purchasing_analysis["Total de Vendas"].map("${:,.2f}".format)
gender_purchasing_analysis ["Total Normalizado"] = gender_purchasing_analysis["Total Normalizado"].map("${:,.2f}".format)

gender_total_item_price
gender_average_item_price
gender_purchasing_analysis

normalized_total

player_demographics

# Cálculos básicos
age_bins = [0, 9.99, 14.99, 19.99, 24.99, 29.99, 34.99, 39.99, 999]
age_bracket = ["Menos de 10", "10 a 14", "15 a 19", "20 a 24", "25 a 29", "30 a 34", "35 a 39", "Mais de 40"]

purchase_file["Range de Idades"] = pd.cut(purchase_file["Idade"], age_bins, labels=age_bracket)

# Cálculos básicos
age_demographics_count = purchase_file["Range de Idades"].value_counts()
age_demographics_average_item_price = purchase_file.groupby(["Range de Idades"]).mean()["Valor"]
age_demographics_total_item_price = purchase_file.groupby(["Range de Idades"]).sum()["Valor"]
age_demographics_percent = (age_demographics_count / player_count) * 100

# Dataframe para os resultados
age_demographics = pd.DataFrame({"Contagem": age_demographics_count, "%": age_demographics_percent, "Valor Unitario": age_demographics_average_item_price, "Valor Total de Compra": age_demographics_total_item_price})

# Data Munging
age_demographics ["Valor Unitario"] = age_demographics["Valor Unitario"].map("${:,.2f}".format)
age_demographics ["Valor Total de Compra"] = age_demographics["Valor Total de Compra"].map("${:,.2f}".format)
age_demographics ["%"] = age_demographics["%"].map("{:,.2f}%".format)

player_demographics.head()
age_demographics = age_demographics.sort_index()
age_demographics

# Cálculos básicos
user_total = purchase_file.groupby(["Login"]).sum()["Valor"].rename("Valor Total de Compra")
user_average = purchase_file.groupby(["Login"]).mean()["Valor"].rename("Valor Médio de Compra")
user_count = purchase_file.groupby(["Login"]).count()["Valor"].rename("Número de Compras")

# Dataframe para os resultados
user_data = pd.DataFrame({"Valor Total de Compra": user_total, "Valor Médio de Compra": user_average, "Número de Compras": user_count})

# Data Munging
user_data ["Valor Total de Compra"] = user_data["Valor Total de Compra"].map("${:,.2f}".format)
user_data ["Valor Médio de Compra"] = user_data["Valor Médio de Compra"].map("${:,.2f}".format)
user_data.sort_values("Valor Total de Compra", ascending=False).head(5)

user_data

# Cálculos básicos
user_total = purchase_file.groupby(["Nome do Item"]).sum()["Valor"].rename("Valor Total de Compra")
user_average = purchase_file.groupby(["Nome do Item"]).mean()["Valor"].rename("Valor Médio de Compra")
user_count = purchase_file.groupby(["Nome do Item"]).count()["Valor"].rename("Número de Compras")

# Dataframe para os resultados
user_data = pd.DataFrame({"Valor Total de Compra": user_total, "Valor Médio de Compra": user_average, "Número de Compras": user_count})

# Data Munging
user_data ["Valor Total de Compra"] = user_data["Valor Total de Compra"].map("${:,.2f}".format)
user_data ["Valor Médio de Compra"] = user_data["Valor Médio de Compra"].map("${:,.2f}".format)
user_data.sort_values("Número de Compras", ascending=False).head(5)

# Cálculos básicos
user_total = purchase_file.groupby(["Nome do Item"]).sum()["Valor"].rename("Valor Total de Compra")
user_average = purchase_file.groupby(["Nome do Item"]).mean()["Valor"].rename("Valor Médio de Compra")
user_count = purchase_file.groupby(["Nome do Item"]).count()["Valor"].rename("Número de Compras")

# Dataframe para os resultados
user_data = pd.DataFrame({"Valor Total de Compra": user_total, "Valor Médio de Compra": user_average, \
                          "Número de Compras": user_count})

# Data Munging
user_data ["Valor Total Compra"] = user_data["Valor Total de Compra"]
user_data ["Valor Total de Compra"] = user_data["Valor Total de Compra"].map("${:,.2f}".format)
user_data ["Valor Médio de Compra"] = user_data["Valor Médio de Compra"].map("${:,.2f}".format)


# display(user_data.sort_values("Valor Total Compra", ascending=False).head(5)[ \
#     ['Valor Total de Compra','Valor Médio de Compra','Número de Compras']])