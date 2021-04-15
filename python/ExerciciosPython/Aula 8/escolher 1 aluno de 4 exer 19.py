'''
import random #importei a função random
n = random.randrange(1, 5) #coloquei para gerar numeros aleatorios de 1 a 5
print(n)
if n == 1:
    print('o escolhido foi Roniel')
elif n == 2:     # o elif funciona como else if(se encontrar uma condição verdadeira ele ezecuta o bloco e para a verificação)
    print('o escolhido foi Fernanda')

elif n == 3:
    print('o escolhido foi o João Miguel')
elif n == 4:
    print('o escolhido foi a Hanah')
else: # sera ezecutado caso nenhuma das condições a sima não forem atendidas
    print('ninguem foi escolhido')

'''

#---------------------------------------------------------------------------------------------------

import random

n1 = str(input('digite nome para o sorteio'))
n2 = str(input('digite nome para o sorteio'))
n3 = str(input('digite nome para o sorteio'))

lista = [n1, n2, n3]
escolhido = random.choice(lista)

print('o escolhido é: {}'.format(escolhido))
