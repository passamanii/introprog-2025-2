n = 0
even = []

def main():

    while (1):

        n = int(input('Digite o número aqui:'))

        if (n == 0):
            break

        if (n // 2 == 0):
            even.append(n)

    process()


def process():

    k = len(even)

    if (k == 0):

        print('Não houve nenhum número par informado.')

    else:
        media = sum(even) / k

        print (f'A média dos valores pares informados é de: {media}')

main()