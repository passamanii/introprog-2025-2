#Quanto maior for o valor de n, mais próximo o resultado chegará de e^x.

def main():

    x = int(input('Informe o valor a ser calculado:'))
    n = int(input('Informe o valor n para a sequência de Taylor:'))

    e = process(x, n)
    print(f'e^{x} é igual à: {e}')



def process(expoente, number):

    soma = 1

    for i in range(1, number):

        soma += (expoente ** i) / fatorial(i)

    return soma



def fatorial(number):

    factor = 1    

    for i in range(1, number + 1):

        factor *= i

    return factor


main()
