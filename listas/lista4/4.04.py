def main():

    A = []

    for i in range(30):
        
        n = float(input('Informe o número desejado:'))
        A.append(n)

    for i in A:

        METADE(i)


def METADE(number):

    value = number / 2

    print(f'A metade de {number} é: {value}.')


main()
