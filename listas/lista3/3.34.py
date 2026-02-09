def main():

    q = int(input('Informe a quantidade de números à serem informados:'))

    for i in range(q):

        n = int(input('Digite aqui:'))

        if (n % 2 == 0):

            div = divisores(n)
            print(f'O número {n} tem {div} divisores.')

        elif (n % 2 == 1 and n < 10):

            fat = fatorial(n)
            print(f'O fatorial de {n} é: {fat}.')

        else:

            som = soma(n)
            print(f'A soma dos inteiros de 1-{n} é: {som}.')


def divisores(number):

    divisores = 0
    
    for i in range(1, number + 1):

        if (number % i == 0):

            divisores += 1

    return divisores


def soma(number):

    soma = 0
    
    for i in range(1, number + 1):

        soma += i

        return soma

def fatorial(number):

    value = 1

    for i in range(1, number + 1):

        value *= i

    return value


main()