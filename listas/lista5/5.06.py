def main():

    A = []

    for i in range(5):

        A += [int(input(f'Digite o número aqui:'))]

    print(f'A lista é: {A}.')

    pares_somados, impares_somados = soma(A)

    print(f'A soma dos números pares da lista é: {pares_somados}.\nA soma dos números ímpares da lista é: {impares_somados}.')

def soma(lista):

    somap = 0
    somai = 0

    for i in lista:

        if (i % 2 == 0):

            somap += i

        else:

            somai += i

    return somap, somai

main()
                        
                    