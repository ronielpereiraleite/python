nome = input('digite seu nome completo\n\t')

print(nome.find('pereira')) # retorna a posição onde comessa a palavra procurada CASO NÃO ENCONTRE RETORNA -1

print(nome.upper().find('PEREIRA')) # PASSEI TUDO PARA MAIUSCULO PARA NÃO DIFEREENCIAR MAIUSCULO DE MINUSCULO

print('pereira' in nome) # retorna true ou false

if nome.upper().find('PEREIRA') >=0:
    print('''\n------------------------------------------------------------------------------------------------ 
    Parabens!!!!
                seu nome contem a palavra Pereira!\n------------------------------------------------------------------------------------------------
    ''')
else:print('seu nome não trem A PALAVRA PEREIRA')