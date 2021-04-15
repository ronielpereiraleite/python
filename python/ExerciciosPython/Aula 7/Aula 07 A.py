n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
r = n1 % n2
print('a soma é: {}\n multiplicação {}\n divisão {:.4f}\n resto da divisão {}\n divisão inteira {}\n exponeciação {}'.format(s,m,d,r,di,e) )