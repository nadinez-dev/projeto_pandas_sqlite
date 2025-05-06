import sqlite3
import pandas as pd

# conecta ou cria banco
con = sqlite3.connect('clinica.db')

# deleta a tabela antiga (se já existir)
con.execute("DROP TABLE IF EXISTS pacientes")

# cria  atabela com a coluna cidade
con.execute('''
CREATE TABLE pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    cidade TEXT
)
''')

# insere dados
con.execute("INSERT INTO pacientes (nome, idade, cidade) VALUES ('Lucas', 32, 'Curitiba')")
con.execute("INSERT INTO pacientes (nome, idade, cidade) VALUES ('Renata', 28, 'São Paulo')")
con.commit()

# le com pandas
df=pd.read_sql_query("SELECT * FROM pacientes", con)
print(df)