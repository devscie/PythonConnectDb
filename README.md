# 🐍 Python & 🎲 SQLite

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-for-VSCode](https://img.shields.io/badge/Made%20for-VSCode-1f425f.svg)](https://code.visualstudio.com/)
[![GitHub license](https://img.shields.io/github/license/devscie/PythonConnectDb)](https://github.com/devscie/PythonConnectDb/blob/master/LICENSE)

## 💻 Sobre o projeto

CRUD em Python e conexão com SQLite

### 🛠 Tecnologias

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org/)
- [SQLite](https://www.sqlite.org/)

Índice de conteúdos
=================
<!--ts-->
   * [Conectando e desconectando do banco](https://github.com/devscie/PythonConnectDb/blob/master/connect_db.py)
   * [Criando um banco de dados](https://github.com/devscie/PythonConnectDb/blob/master/01_create_db.py)
   * [Criando uma tabela](https://github.com/devscie/PythonConnectDb/blob/master/02_create_schema.py)
   * [Comandos](#comandos)
      * [Create - Inserindo 1 registro com comando SQL](https://github.com/devscie/PythonConnectDb/blob/master/03_create_data_sql.py)
      * [Create - Inserindo N registros com uma tupla de dados](https://github.com/devscie/PythonConnectDb/blob/master/04_create_data_nrecords.py)
      * [Create - Inserindo 1 registro com parâmetros de entrada](https://github.com/devscie/PythonConnectDb/blob/master/05_create_data_param.py)
      * [Read - Lendo os dados](https://github.com/devscie/PythonConnectDb/blob/master/06_read_data.py)
      * [Update - Alterando os dados](https://github.com/devscie/PythonConnectDb/blob/master/07_update_data.py)
      * [Delete - Deletando os dados](https://github.com/devscie/PythonConnectDb/blob/master/08_delete_data.py)
      * [Alter - Adicionando uma nova coluna](https://github.com/devscie/PythonConnectDb/blob/master/09_alter_table.py)
   * [Lendo as informações do banco de dados](https://github.com/devscie/PythonConnectDb/blob/master/10_view_table_info.py)
   * [Fazendo backup do banco de dados (exportando dados)](https://github.com/devscie/PythonConnectDb/blob/master/11_backup.py)
   * [Recuperando backup do banco de dados (importando dados)](https://github.com/devscie/PythonConnectDb/blob/master/12_recovery_sql.py)
   * [License](https://github.com/devscie/PythonConnectDb/blob/master/LICENSE)
<!--te-->

### Features

- [x] Cadastrar usuário
- [x] Visualizar usuário
- [x] Atualizar usuário
- [x] Deletar usuário
- [ ] Módulo datetime - Retornar a data e hora local atual

### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Python](https://www.python.org/). 
Além disso um bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

### 💻 Rodando

```bash
# Clone este repositório
$ git clone <https://github.com/devscie/PythonConnectDb>

# Acesse a pasta do projeto no terminal/cmd
$ cd PythonConnectDb

# Criando um banco de dados
$ python3 01_create_db.py
$ ls *.db

# Criando uma tabela
$ python3 02_create_schema.py
$ sqlite3 clientes.db '.tables'
$ sqlite3 clientes.db 'PRAGMA table_info(clientes)'

# Create - Inserindo 1 registro com comando SQL
$ python3 03_create_data_sql.py

# Create - Inserindo N registros com uma tupla de dados
$ python3 04_create_data_nrecords.py

# Create - Inserindo 1 registro com parâmetros de entrada
$ python3 05_create_data_param.py

# Read - Lendo os dados
$ python3 06_read_data.py

# Update - Alterando os dados
$ python3 07_update_data.py

# Delete - Deletando os dados
$ python3 08_delete_data.py

# Alter - Adicionando uma nova coluna
$ python3 09_alter_table.py

# Lendo as informações do banco de dados
$ python3 10_view_table_info.py

# Fazendo backup do banco de dados (exportando dados)
$ python3 11_backup.py
$ cat clientes_dump.sql

# Recuperando backup do banco de dados (importando dados)
$ python3 12_read_sql.py
$ sqlite3 clientes_recuperado.db 'SELECT * FROM clientes;'

```

###	🚧 Python & SQLite (Em construção) 🚧

### Como contribuir para o projeto

1. Faça um **fork** do projeto.
2. Crie uma nova branch com as suas alterações: `git checkout -b my-feature`
3. Salve as alterações e crie uma mensagem de commit contando o que você fez: `git commit -m "feature: My new feature"`
4. Envie as suas alterações: `git push origin my-feature`
>> Caso tenha alguma dúvida confira este [guia de como contribuir no GitHub](https://github.com/firstcontributions/first-contributions)


## Licença

Este projeto esta sobe a licença MIT.

## Autor

<img src="https://avatars3.githubusercontent.com/u/78492236" width="100px;" alt="Avatar" style="border-radius: 50%;">
<b>Vinicius George dos Santos</b>
<br /><br />

👋🏽 Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Vinicius-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/vinicius-george-dos-santos-932b29167/)](https://www.linkedin.com/in/vinicius-george-dos-santos-932b29167/) 
[![Gmail Badge](https://img.shields.io/badge/-devscient@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:devscient@gmail.com)](mailto:devscient@gmail.com)
