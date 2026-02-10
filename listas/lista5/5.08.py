import random

def main():
    
    qx = 0
    L = []
    found = False

    for i in range(25):

        L.append(random.randint(-20,20))

    x = int(input('Informe o valor que deseja buscar:'))

    print(L)

    for i, v in enumerate(L): 

        if (v == x):

            if (found == False):

                print(f'O número {x} foi encontrado na {i}ª posição.')

            qx += 1

    if (qx == 0):

        print(f'O número {x} não foi encontrado na lista.')

    else:

        print(f'O valor {x} foi encontrado {qx} vezes na lista.')


main()


