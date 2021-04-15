frase = input('digite uma frase:\n\t')
procura = 'a'
tamam = len(frase)


print('a letra {} aparece na frase {} vezes\n'.format(procura,frase.count(procura)))

print('a letra {} aparece pela primeira vez na posição: {}'.format(procura, frase.find(procura)))


for i in range(0, tamam):
    if frase[i] == procura:
        print('na pasição {}'.format(i))

