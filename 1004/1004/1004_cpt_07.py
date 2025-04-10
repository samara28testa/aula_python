import pandas as pd

import numpy as np

import random

# Esercizio 1: Analisi Esplorativa dei Dati:

# 1: Caricare i Dati in un DataFrame autogenerandoli casualmenti.

data= {
    'Nome': ['Alice', 'Bob', 'Carla', 'Michel', 'Carlo', 'Francesco', 'Rafael'],
    'Età': np.linspace(0, 70, 7, dtype=int),
    'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma', 'Roma'],
    'Salario': np.linspace(0, 40000, 7, dtype=int)
}

df = pd.DataFrame(data)

# Stampa del DataFrame originale

print("DataFrame originale")
print(df)

# Visualizzare le prime e le ultime cinque righe del DataFrame

riga = df.iloc[0:1]

riga_5 = df.iloc[-5:]

print("Le prime righe")
print(riga)
print("Le ultime 5 righe")
print(riga_5)

# Visualizzare il tipo di dati di ciascuna colona

df_type = df.dtypes
print("Tipo di dati:")
print(df_type)

# Calcolarestatistiche descritive di base

media_eta = df['Età']. mean()
mediana_eta = df['Età'].median()
std_eta = df['Età'].std()

salario_media = df['Salario']. mean()
salario_mediana = df['Salario'].median()
salario_std = df['Salario'].std()

print("Statistica della età")
print("Media",media_eta,"Mediana", mediana_eta, "Std", std_eta)

print("Statistica del Salario")
print("Media",salario_media,"Mediana", salario_mediana, "Std", salario_std)

# Duplicati

df = df.drop_duplicates()

df_cleaned =df.dropna()

# Mancanti

df['Età'] = df['Età'].replace(0, media_eta)
df['Salario'] = df['Salario'].replace(0, salario_media)

df['Età'] = df['Età'].astype(int)
df['Salario'] = df['Salario'].astype(int)

print("\nDataFrame dopo la pulizia:")
print(df)

# Categoria Età

for index, row in df.iterrows():  
    if 18 <= row['Età'] < 65:
        print(f"{row['Nome']} è un Adulto")
    else:
        print(f"{row['Nome']} è un Senior")
        
# Salvataggio 
df.to_csv('dataframe_pulito.csv', index=False)