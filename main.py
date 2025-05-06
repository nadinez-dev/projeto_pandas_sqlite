import sqlite3
import pandas as pd

con = sqlite3.connect('clinica.db')

con.execute("DROP TABLE IF EXISTS pacientes")

con.execute('''
CREATE TABLE pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    cidade TEXT
)
''')
con.execute("INSERT INTO pacientes (nome, idade, cidade) VALUES ('Lucas', 32, 'Curitiba')")
con.execute("INSERT INTO pacientes (nome, idade, cidade) VALUES ('Renata', 28, 'São Paulo')")
con.commit()

df=pd.read_sql_query("SELECT * FROM pacientes", con)
print(df)