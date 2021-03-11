# 03_create_data_sql.py
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# inserindo dados na tabela
cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Afonso', 50, '00000000000', 'afonso@email.com', '31-98765-4321', 'Belo Horizonte', 'MG', '2014-06-08')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Julio', 47, '11111111111', 'julio@email.com', '11-98765-4322', 'São Paulo', 'SP', '2014-06-09')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Baltazar', 53, '22222222222', 'baltazar@email.com', '21-98765-4323', 'Rio de Janeiro', 'RJ', '2014-06-09')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Getulio', 45, '33333333333', 'getulio@email.com', '27-98765-4324', 'Vitória', 'ES', '2014-06-08')
""")

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()