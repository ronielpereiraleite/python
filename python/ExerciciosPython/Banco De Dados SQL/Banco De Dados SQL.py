import mysql.connector   # criar banco de dados todos os videos:  https://www.youtube.com/watch?v=sO-HDU3XqbQ&list=PLwsAoT89dh3pL8Zgp1gxYeoew5Tm19BIs

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="python_yotube"
)
rep = int(1)
while rep >= 1:
    cursor = banco.cursor()

    print('\n'*5,'\t\t####################'
                 '\n\t\t#  0 - para sair '
                 '\n\t\t#  1 - para mostra'
                 '\n\t\t#  2 - para inserir  '
                 '\n\t\t#  3 - para execlui '
                 '\n\t\t#  4 - para '
                 '\n\t\t#  5 - para '
                 '\n\t\t####################')
    op = int(input('\t\t digite uma opção do menu: '))
    rep = op
    #cursor.execute("CREATE DATABASE python_yotube") # criei o banco python_yotube
    #cursor.execute("CREATE TABLE pessoas(nome VARCHAR(255),idade INT(3),email VARCHAR(255))") # criei a tabela pessoas dentro de python_yotube

  #  cursor.execute("CREATE TABLE objeto(cod INT(),nome VARCHAR(255),idade INT(3),email VARCHAR(255))")

    if op == 1: # mostra todos os dados da tabela pessoas
        comando_sql = "SELECT * FROM pessoas"
        cursor.execute(comando_sql)
        valores_lidas = cursor.fetchall()
        print(valores_lidas)

    elif op == 2: # enserir dados na tabela pessoas
        comando_sql = "INSERT INTO pessoas (nome,idade,email) VALUES (%s,%s,%s)" # essas 6 linhas são usadas para enserir dados na tabela pessoas
        nome = input("digite nome")
        idade = input("digite idade")
        email = input("digite E-mail")
        dados = (nome, idade, email)
        cursor.execute(comando_sql, dados)

    elif op == 3: # execlui dados da tabela pessoas     https://www.youtube.com/watch?v=d1R1p9pY7qM




        apag = 'DELETE FROM pessoas WHERE nome='+id

        id = (input('digite nome a ser apagado'))



        cursor.execute(apag,id)
        cursor.commit()


            # apag = "DELETE FROM pessoas WHETE (nome) VALUES "  #essa e as 2 linhas de baixo estava funcionando
           # nom = input('digite nome a ser DELETADO')
            # cursor.execute(apag, nom)


       # comando_sql = "DELETE FROM pessoas WHERE nome = 'Roniel'" # não esta asseitando colocar dados pela variavel
       # cursor.execute(comando_sql)
       # banco.commit()


    else:
        print('OPÇÃO INCORRETA!!\t TENTE NOVAMENTE\n\n\n\n')




    #  PAREI NESTE VIDEO       https://www.youtube.com/watch?v=d1R1p9pY7qM
    # AULA 05



