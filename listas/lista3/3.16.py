def main():

    n = int(input('Insira o número desejado:'))

    factorial(n)

    while(1):

        again = input('Deseja calcular o fatorial de outro número? Sim(S) Não(N):').upper()

        if (again == 'S'):

            n = int(input('Insira o número desejado:'))

            factorial(n)

        else:

            print('Obrigado por utilizar os sistemas Oscorp! Aplicativo finalizado.')

            break


def factorial(number):

    factor = 1
    
    for i in range(1, number + 1):

        factor *= i 

    print(f'O fatorial de {number} é: {factor}.')


main()