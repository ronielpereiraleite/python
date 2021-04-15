nome = input('digite seu nome completo:\n\t ')
fatia = nome.split()

tam = len(fatia)

print('primeiro nome: {}\nsegundo nome: {}'.format(fatia[0], fatia[tam -1]))