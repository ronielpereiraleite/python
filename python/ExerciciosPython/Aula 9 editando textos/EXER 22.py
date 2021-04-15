nome = input('qual seu nome completo? \n').strip() # colocando .strip() elimina os espaços no inicio e no fim da strig
print(nome.upper()) # tudo maiusculo
print(nome.lower()) # tudo minusculo
print(nome.title()) # so as primeiras letras são maiusculas

separa = nome.split()  # separando e guardando em uma variavel

#junta = ''.join(separa)
#print('a palavra {} sem os espaços {} trem {}'.format(nome, ''.join(separa), len(junta)))

print('a palavra {} sem os espaços {} trem {} caracteres'.format(nome, ''.join(separa), len(''.join(separa))))

print('O seu primeiro nome {} tem {} letras, e o seu nome conpleto tem {} letras'.format(separa[0].title(), len(separa[0]), len(nome) - nome.count(' '))) # mostrando o primeiro nome com a primeira letra maiuscula