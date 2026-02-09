def main():

    a, b = map(int, input('Informe o 1º intervalo (X,Y):').split(','))
    c, d = map(int, input('Informe o 2º intervalo (X,Y):').split(','))
    e, f = map(int, input('Informe o 3º intervalo (X,Y):').split(','))
    g, h = map(int, input('Informe o 4º intervalo (X,Y):').split(','))
    i, j = map(int, input('Informe o 5º intervalo (X,Y):').split(','))
   
    i1 = []
    i2 = []
    i3 = []
    i4 = []
    i5 = []

    for z in range(a, b+1):

        if (z % 2 == 0):

            i1.append(z)

    
    for z in range(c, d + 1):

        if (z % 2 == 0):

            i2.append(z)

    
    for z in range(e, f + 1):

        if (z % 2 == 0):

            i3.append(z)

    
    for z in range(g, h + 1):

        if (z % 2 == 0):

            i4.append(z)

    
    for z in range(i, j + 1):

        if (z % 2 == 0):

            i5.append(z)

    
    print(f'\nOs números pares no intervalo {a}-{b} são: {i1}.')
    print(f'Os números pares no intervalo {c}-{d} são: {i2}.')
    print(f'Os números pares no intervalo {e}-{f} são: {i3}.')
    print(f'Os números pares no intervalo {g}-{h} são: {i4}.')
    print(f'Os números pares no intervalo {i}-{j} são: {i5}.')


main()