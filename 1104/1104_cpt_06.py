import sqlite3

conn = sqlite3.connect("scuola.db")

cur = conn.cursor()

nome = [ ("Claudio",), ("Ricardo",)]
cur.executemany("INSERT INTO studenti (nome) VALUES (?)", nome)

cur.execute("SELECT * FROM studenti")
righe = cur.fetchall()

for riga in righe:
    print(riga)

conn.commit()
conn.close()
