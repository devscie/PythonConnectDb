# 03_create_data_sql.py
import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# inserindo dados na tabela
cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Afonso', 50, '00000000000', 'afonso@email.com', '31-98765-4321', 'Belo Horizonte', 'MG', '2021-03-11')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Baltazar', 47, '11111111111', 'baltazar@email.com', '21-98765-4322', 'Rio de Janeiro', 'RJ', '2021-03-12')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Joaquim', 45, '22222222222', 'joaquim@email.com', '11-98765-4323', 'São Paulo', 'SP', '2021-03-13')
""")

cursor.execute("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES ('Getulio', 54, '33333333333', 'getulio@email.com', '27-98765-4324', 'Vitória', 'ES', '2021-03-14')
""")

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()