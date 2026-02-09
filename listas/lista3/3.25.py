def main():

    n1 = int(input('Insira o 1º número:'))
    n2 = int(input('Insira o 2º número:'))
    n3 = int(input('Insira o 3º número:'))
    n4 = int(input('Insira o 4º número:'))
    n5 = int(input('Insira o 5º número:'))

    print(f'\n---Tabuada de {n1}---\n')
    for i in range(1, n1 + 1):

        prod = i * n1
        print(f'{i} x {n1} = {prod}')

    print(f'\n---Tabuada de {n2}---\n')
    for i in range(1, n2 + 1):

        prod = i * n2
        print(f'{i} x {n2} = {prod}')

    print(f'\n---Tabuada de {n3}---\n')
    for i in range(1, n3 + 1):

        prod = i * n3
        print(f'{i} x {n3} = {prod}')

    print(f'\n---Tabuada de {n4}---\n')
    for i in range(1, n4 + 1):

        prod = i * n4
        print(f'{i} x {n4} = {prod}')

    print(f'\n---Tabuada de {n5}---\n')
    for i in range(1, n5 + 1):

        prod = i * n5
        print(f'{i} x {n5} = {prod}')

    
main()