x = float (input ('Insira o valor inicial:'))
y = float (input ('Insira o valor final:'))
z = x

while (y < x):
    print ('Intervalo inválido. Digite novamente.')
    x = float (input ('Insira o valor inicial:'))
    y = float (input ('Insira o valor final:'))

while (z <= y):

    if (z % 2 == 0):
        print (f'{int(z):02d}')
    
    z += 1


