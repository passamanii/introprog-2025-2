def main():

    teta = float(input('Informe o ângulo em radianos:'))

    cos = process(teta)
    print(f'O cosseno de {teta}rad é: {(cos):.2f}')



def process(degree):

    soma = 1

    for i in range(2, 40, 2):

        pol = (i // 2)

        if (pol % 2 == 0):

            soma += (degree ** i) / fatorial(i)

        else:

            soma -= (degree ** i) / fatorial(i)

    return soma




def fatorial(number):

    product = 1

    for i in range(1, number + 1):
        
        product *= i

    return product


main()