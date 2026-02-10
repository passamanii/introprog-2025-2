import random

def main():

    G = []

    for i in range(13):

        G.append(random.randint(0,2))

    for i in range(10):

        R = []
        acertos = 0
        code = int(input('Informe o código do apostador:'))

        for i in range(len(G)):

            R.append(random.randint(0,2))

            if (R[i] == G[i]):

                acertos += 1

        print(f'Gabarito: {G}')
        print(f'Respostas: {R}')
        print(f'O apostador {code} acertou {acertos} apostas!')

    print('Programa encerrado.')


main()


    