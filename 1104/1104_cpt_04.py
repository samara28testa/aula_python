import sqlite3  # Importa il modulo per lavorare con SQLite

# 1. Connessione (crea un file 'scuola.db' se non esiste)
conn = sqlite3.connect('scuola.db')

# 2. Cursore per eseguire comandi SQL
cur = conn.cursor()

# 3. Creazione di una tabella (se non esiste)
cur.execute('''
    CREATE TABLE IF NOT EXISTS studenti (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT
    )
''')

# 4. Inserimento di un dato
cur.execute("INSERT INTO studenti (nome) VALUES (?)", ("Francesco",))
cur.execute("INSERT INTO studenti (nome) VALUES (?)", ("Lorenza",))
cur.execute("INSERT INTO studenti (nome) VALUES (?)", ("Danilo",))

# 5. Salvataggio delle modifiche
conn.commit()

# 6. Query per leggere i dati
cur.execute("SELECT * FROM studenti")
righe = cur.fetchall()

# 7. Stampa dei risultati
for riga in righe:
    print(riga)
    
conn.commit()

conn.close()