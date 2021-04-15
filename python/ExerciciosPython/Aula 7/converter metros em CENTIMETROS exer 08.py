n = float(input('digite metros a serem convertidos:\n\t'))

# print("\nCentimertos: \t", n * 100, '\nMilimitros: \t', n * 1000)
# print('\nCentimertos: \t{:.2f}\nMilimitros: \t{:.2f}'.format(n*100, n*1000))

print('\nCentimertos:{:->18}\nMilimitros:--{:->18}'.format(n*100, n*1000))