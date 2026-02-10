import random

def main():

    D = []

    for i in range(60):

        D += [random.randint(-100,100)]

    print(f'Lista Normal: {D}')

    for i in range(len(D)):

        if (i <= 29):
                
            temp = D[30 + i]

            D[30 + i] = D[i]
            D[i] = temp

    print(f'Lista Invertida: {D}')

main()