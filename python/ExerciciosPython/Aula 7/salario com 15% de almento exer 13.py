n = float(input('qual seu salario? '))

#print('você teve um almento de R$ {:.2f} \t salario total e: R$ {:.2f}'.format(n * .15,n + (n * .15)))

print('você teve um almento de R$ {:.2f} \t salario total e: R$ {:.2f}'.format(n * 15 / 100, n + (n * .15)))