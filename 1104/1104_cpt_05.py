import sqlite3 

conn = sqlite3.connect('scuola.db')

cur = conn.cursor()

cur.execute("SELECT * FROM studenti")
righe = cur.fetchall()

for riga in righe:
    print(riga)

cur.execute("INSERT INTO studenti (nome) VALUES (?)", ("Victor",))   
cur.execute("INSERT INTO studenti (nome) VALUES (?)", ("Chiara",))

righe = cur.fetchall()

cur.execute("SELECT * FROM studenti")
righe = cur.fetchall()

for riga in righe:
    print(riga)
    
cur.execute("DELETE FROM studenti WHERE ID = ?", (4,))
conn.commit()

cur.execute("SELECT * FROM studenti")
righe = cur.fetchall()

for riga in righe:
    print(riga)

conn.commit()
conn.close()