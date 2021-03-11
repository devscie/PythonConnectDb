# Podemos criar o banco de dados de duas formas: na memória RAM (':memory:')
# ou persistindo em um banco de dados ('clientes.db')
# conectando...
conn = sqlite3.connect('clientes.db')