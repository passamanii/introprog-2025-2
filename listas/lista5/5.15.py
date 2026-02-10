import random

def main():

    X = []
    V = []

    for i in range(10):

        X.append(random.randint(0,2000))
        V.append(random.randint(-2000, 0))

    S = [] + X + V 

    print(f'Lista S: {S}.')
    print(f'Lista S Ordenada: {sorted(S)}.')


main()