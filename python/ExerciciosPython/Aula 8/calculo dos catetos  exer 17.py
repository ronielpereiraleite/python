'''

oposto = float(input('digite o cateto oposto'))
adijacente = float(input('digite o cateto oposto'))

ipotenusa = ((oposto ** 2 + adijacente ** 2) ** (1/2))

print('a ipotenusa é: {:.2f}'.format(ipotenusa))
'''

# com a função math
import math

oposto = float(input('digite o cateto oposto'))
adijacente = float(input('digite o cateto oposto'))

ipotenusa = math.hypot(oposto, adijacente)

print('a ipotenusa é: {:.2f}'.format(ipotenusa))