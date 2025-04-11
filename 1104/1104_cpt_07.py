import sqlite3
import random

# Scrivi un programma Python che gestisca una picola libreria usando un database SQLit

# creazione della classe di libro

class Libro:
    
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore
      
# creazione del database
conn = sqlite3.connect('libreria.db')

cur = conn.cursor()
    
cur.execute('''
CREATE TABLE IF NOT EXISTS libri (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titolo TEXT,
        autore
)
''')
    
# creazione di elementi

libri = [
    Libro("Il nome dellla rosa", "Umberto Eco"),
    Libro("1984", "George Orwel"),
    Libro("Orgoglio e pregiudizio", "Jane Austen")
]

dati_libri = [(libro.titolo, libro.autore) for libro in libri]

cur.executemany("INSERT INTO libri (titolo, autore) VALUES (?, ?)", dati_libri)

conn.commit()

cur.execute("SELECT * FROM libri")
righe = cur.fetchall()

for riga in righe:
    print(riga)
    
cur.execute("ALTER TABLE libri ADD COLUMN vendite INTEGER")
conn.commit()

cur.execute("SELECT * FROM libri")
righe = cur.fetchall()

for riga in righe:
    print(riga)
    
cur.execute("SELECT id FROM libri")
id_libri = cur.fetchall()


for id in id_libri:
    vendite = random.randint(10, 20)
    cur.execute("UPDATE libri SET vendite = ? WHERE id=?", (vendite, id[0]))
    
conn.commit()

cur.execute("SELECT * FROM libri")
righe = cur.fetchall()

for riga in righe:
    print(riga)
    
conn.close()