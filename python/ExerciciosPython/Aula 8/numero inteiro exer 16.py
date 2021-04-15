'''    #com as 3 aspas simples eu comento umtrexo do codigo
n = float(input('digite valor a ser arredondad')) #NUMERO A SER ARREDONDADO
print('numero a ser arredondado: ', n, 3 * '\n')

print(round(n)) # ARREDONDA O NUMERO PARA O NUMERO PAR MAIS PROXIMO
print(round(n, 2))  #o numero 2 é a quantidade de casas apos a virgula

print('para baixo', round(n - 0.5))
print('para sima', round(n + 0.5))
'''
#-----------------------------------------------------------------------------

'''
import math
n = float(input('digite numero a ser arredondado: '))

print('o numero: {} \narredondado fica {}'.format(n, math.trunc(n)))
'''
#------------------------------------------------------------------------------

n = float(input('digite um numero a ser arredondado: '))

print('o numero {} arredondado fica: {}'.format(n,int(n)))

num = int(n) # da ate para converter em inteiro ('-')
print(num)