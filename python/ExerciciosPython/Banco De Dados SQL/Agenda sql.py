import mysql.connector   # criar banco de dados todos os videos:  https://www.youtube.com/watch?v=sO-HDU3XqbQ&list=PLwsAoT89dh3pL8Zgp1gxYeoew5Tm19BIs

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="Agenda"  # esta linha não pode estar visivel quando for criar o banco
)

cursor = banco.cursor()

#cursor.execute("CREATE DATABASE Agenda") # criei o banco

#cursor.execute("CREATE TABLE pessoas(nome VARCHAR(255),idade INT(3),email VARCHAR(255))")
#cursor.execute("CREATE TABLE teste(id INT(10) NOT NULL AUTO_INCREMENT, nome VARCHAR(20),primary key (id))")
#cursor.execute("CREATE TABLE pessoas(id INT(10) unsigned not null auto_increment,nome VARCHAR(60) not null,endereco VARCHAR(50) not null,email VARCHAR(40) not null,telefone VARCHAR(15) not null,primary key (id)");  # criei a tabela pessoas dentro de python_yotube

#cursor.execute("create table pessoas(id int(10) unsigned not null auto_increment,nome varchar(60) not null,endereco varchar(50) not null,email varchar(40) not null,telefone varchar(15) not null,primary key (id)")

op = int(input('digit 1 ou 2'))

if op == 1:  # mostra todos os dados da tabela pessoas
    comando_sql = "SELECT * FROM teste"
    cursor.execute(comando_sql)
    valores_lidas = cursor.fetchall()
    print(valores_lidas)

if op == 2:  # enserir dados na tabela pessoas
    comando_sql = "INSERT INTO pessoas (id,nome) VALUES (%s,%s)"  # essas 6 linhas são usadas para enserir dados na tabela pessoas
    nome = input("digite nome")
   # idade = input("digite idade")
    #email = input("digite E-mail")
    dados = (nome)
    cursor.execute(comando_sql, dados)