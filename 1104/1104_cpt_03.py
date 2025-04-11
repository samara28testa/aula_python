import sqlite3  # Importa il modulo per lavorare con SQLite

# 1. Connessione (crea un file 'miodatabase.db' se non esiste)
conn = sqlite3.connect('miodatabase_2.db')

# 2. Cursore per eseguire comandi SQL
cur = conn.cursor()

# 6. Query per leggere i dati
cur.execute("SELECT * FROM utenti_2")
righe = cur.fetchall()

# 7. Stampa dei risultati
for riga in righe:
    print(riga)

cur.execute("DELETE FROM utenti_2 WHERE id =?", (1,))
conn.commit()

conn.close()