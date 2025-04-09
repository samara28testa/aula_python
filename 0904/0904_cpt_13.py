import pandas as pd

# import di un file con Pandas

# percorso del file csv

file_path = 'data.csv'

# Caricamento dei dati nel DataFrame

df = pd.read_csv('0904\data.csv')

# le prime righe del DataFrame per confermare

print(df.head())