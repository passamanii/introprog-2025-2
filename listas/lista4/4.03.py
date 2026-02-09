def main():

    n = int(input('Informe um valor:'))

    s = TROCA(n)

    if (s == 'Positivo'):

        print(f'{n} é maior que 0.')

    elif (s == 'Negativo'):

        print(f'{n} é menor que 0.')

    else:

        print(f'{n} é igual à 0.')


def TROCA(number):

    if (number > 0):

        value = 'Positivo'

    elif (number < 0):

        value = 'Negativo'

    else:

        value = 'Zero'

    print(f'{value}.')

    return value

main()