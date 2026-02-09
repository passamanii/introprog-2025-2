def main():

    while (1):

        n = int(input('Informe um número ímpar:'))

        if (n % 2 == 1):

            break

        else:

            print('Número inválido. Tente novamente.')
            continue

    teta = float(input('Informe o grau em radianos:'))

    
    process(n, teta)
   


def process(number, degrees):

    seno = degrees

    for i in range(3, number + 1, 2):

        if (i % 4 == 1):

            seno += ((degrees ** i) / fatorial(i))

        else:
            
            seno -= ((degrees ** i) / fatorial(i))


    print(f'O seno do ângulo {(degrees):.2f}rad é: {(seno):.2f}.')
 


def fatorial(number):

    fator = 1

    for i in range(1, number + 1):

        fator *= i 

    return fator

main()