import random

def main():

    L = []
    quant = 0

    for i in range(5):

        L.append(random.randint(0,5))

    print(L)

    for ind1, i in enumerate(L):

        for ind2, j in enumerate(L):

            if (ind1 != ind2 and ind1 < ind2):
                    
                if (i == j):

                    print(f'O número {i} foi encontrado na {ind2 + 1}ª posição!')


main()