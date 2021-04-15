d = int(input('quantos dis o carro ficol alugado? '))
k = int(input('quantos quilometros o carro andou? '))
print('o valor a ser pago é: R$ {:.2f}'.format((d * 60) + (k * .15)))

# 60 reais por dia e 0.15 por quilometros