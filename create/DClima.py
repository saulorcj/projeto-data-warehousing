import pandas as pd
import random as rd


# Função para categorizar temperatura
def categorizar_temp(temp):
    if temp < 7:
        return 'Frio'
    elif 7 <= temp < 13:
        return 'Fresca'
    elif 13 <= temp < 18:
        return 'Amena'
    elif 18 <= temp < 24:
        return 'Agradavel'
    elif 24 <= temp < 29:
        return 'Morna'
    elif 29 <= temp < 35:
        return 'Quente'
    else:
        return 'Escaldante'

# Função para categorizar umidade
def categorizar_ur(ur):
    if ur < 30:
        return 'Muito Baixa'
    elif 30 <= ur < 40:
        return 'Baixa'
    elif 40 <= ur < 60:
        return 'Moderada'
    elif 60 <= ur < 80:
        return 'Alta'
    else:
        return 'Muito Alta'


# Lê o arquivo CSV
df = pd.read_csv('../base/Base.csv')


# Aplica a categorização
df['temp'] = df['temp'].apply(categorizar_temp)
df['ur'] = df['ur'].apply(categorizar_ur)

DClima = pd.DataFrame()

DClima['temperatura'] = df['temp']
DClima['umidade'] = df['ur']

DClima = DClima.drop_duplicates()

chaves_unicas = set()

DClima['pk_clima'] = range(1, len(DClima)+ 1)




DClima.to_csv('../Dim/DClima.csv', index=False)
