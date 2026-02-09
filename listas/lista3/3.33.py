def main():

    q = int(input('Informe a quantidade de valores à serem inseridos:'))

    for i in range(q):

        n = int(input('Digite o número aqui:'))

        fator = fatorial(n)

        print(f'O valor é: {n}.\nO fatorial de {n} é {fator}.')




def fatorial(number):

    value = 1

    for i in range(1, number + 1):

        value *= i

    return value


main()