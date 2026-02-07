x = float (input ('Insira o valor inicial:'))
y = float (input ('Insira o valor final:'))

while (y < x):
    print ('Intervalo inválido. Digite novamente.')
    x = float (input ('Insira o valor inicial:'))
    y = float (input ('Insira o valor final:'))

while (x <= y):

    print (f'{(x):.0f}')
    x += 1

