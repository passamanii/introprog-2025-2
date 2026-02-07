def main():

    somatorio = 0

    n = int(input('Informe o número desejado:'))

    for i in range(n + 1):

        somatorio += 1 / fatorial(i)

    print(f'O resultado da função (S) é: {(somatorio):.2f}.')


def fatorial(number):

    fator = 1

    for i in range(1, number + 1):

        fator *= i

    return fator 



main()