#resposta do professor

num = int(input('digite um numero: \n'))

n1 = num // 1 % 10
n2 = num // 10 % 10
n3 = num // 100 % 10
n4 = num // 1000 % 10

print('unidade:{}'.format(n1))
print('desena:{}'.format(n2))
print('sentena:{}'.format(n3))
print('milhar:{}'.format(n4))

'''     # minha solução
num = input('digite um numero:\n')
quant = len(num)

if quant > 0:
    print('unidade: {}'.format(num[quant -1]))
    if quant > 1:
        print('dezena: {}'.format(num[quant -2]))
        if quant > 2:
            print('Centena: {}'.format(num[quant -3]))
            if quant > 3:
                for i in range(0, quant -3):
                        print('milhar: {}'.format(num[i]))
'''