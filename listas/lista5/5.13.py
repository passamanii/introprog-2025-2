import random

def main():

    G = []
    inteligentes = 0

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

        if (acertos >= 10):

            inteligentes += 1

        burros = 10 - inteligentes

    bpercent = (burros / 10) * 100
    ipercent = (inteligentes / 10) * 100

    print(f'{ipercent}% dos apostadores acertaram mais de 10 apostas.')
    print(f'{bpercent}% dos apostadores acertaram menos de 10 apostas.')


main()


    