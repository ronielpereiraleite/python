# tipos primitivos de dados

n = input('\n\t\tdigite algo:')

print('\nnumerico \t', n.isnumeric())
print('aufabeto \t', n.isalpha())
print('decimal \t', n.isdecimal())
print('somente espaços \t', n.isspace())
print('alfa numerico \t', n.isalnum())
print('esta em maiuscula \t', n.isupper())
print('está em minusculo \t', n.islower())
print('está capitalizada (maiuscula e minuslula) \t', n.istitle())

print('\ntipo da classe: ', type(n))         #usado para saber o tipo da variavel

#terminar aula 6 aos 22.40 minutos