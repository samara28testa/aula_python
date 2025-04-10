import pandas as pd
import numpy as np

# DataFrame esempio, inclusi valori mancanti e duplicati

data= {
    'Nome': ['Alice', 'Bob', 'Carla', 'Bob', 'Carla', 'Alice', None],
    'Età': [25, 30, 22, 30, np.nan, 25, 29],
    'Città': ['Roma', 'Milano', 'Napoli', 'Milano', 'Napoli', 'Roma', 'Roma']
}

df = pd.DataFrame(data)

# Stampa del DataFrame originale

print("DataFrame originale")
print(df)

df = df.drop_duplicates()

df_cleaned =df.dropna()

df['Età'].fillna(df['Età'].mean(), inplace=True)

print("\nDataFrame dopo la pulizia:")
print(df_cleaned)
print("\nDataFrame con dati mancanti sostituitti")
print(df)