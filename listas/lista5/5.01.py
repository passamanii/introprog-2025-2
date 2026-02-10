import random

def main():

    L = []
    neg = 0

    for i in range(6):

        L.append(random.randint(-200, 200))

    for i in L:

        if (i < 0):

            neg += 1

    print(L)
    print(f'Foram lidos {neg} valores negativos.')


main()
