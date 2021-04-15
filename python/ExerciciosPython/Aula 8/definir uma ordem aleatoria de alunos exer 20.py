'''
import random
n = []
nome = ['RONIEL', 'FERNANDA', 'JOÃO MIGUEL', 'HANNAH', 'MELISSA', 'GUILHERME']
pos = [0, 0, 0, 0, 0, 0]
n = random.sample(range(1, 7), 6)

print(2*'\n')



for i in range(0,7): # posição [0]
    #print('valor de i', i)
    if n[0] == i:
        pos[0] = nome[i - 1]
        #print(pos[0])
        break

for i in range(0,7): # posição [1]
    #print('valor de i', i)
    if n[1] == i:
        pos[1] = nome[i - 1]
        #print(pos[1])
        break

for i in range(0,7): # posição [2]
    #print('valor de i', i)
    if n[2] == i:
        pos[2] = nome[i - 1]
        #print(pos[2])
        break

for i in range(0,7): # posição [3]
    #print('valor de i', i)
    if n[3] == i:
        pos[3] = nome[i - 1]
        #print(pos[3])
        break

for i in range(0,7): # posição [4]
    #print('valor de i', i)
    if n[4] == i:
        pos[4] = nome[i - 1]
        #print(pos[4])
        break

for i in range(0,7): # posição [5]
    #print('valor de i', i)
    if n[5] == i:
        pos[5] = nome[i - 1]
        #print(pos[5])
        break

for i in range(0, 6): #mostrar as posições
    print('|\t', i + 1, 'º----', pos[i], '\n###########################')

''' #os dois codigos fazem a mesma coisa
#--------------------------------------------------------------------------------------

import random

n1 = input('digite a primeira pessoa')
n2 = input('digite a segunda pessoa')
n3 = input('digite a terceira pessoa')

lista = [n1, n2, n3]
random.shuffle(lista) # troca os itens da lista de posição
print(lista)