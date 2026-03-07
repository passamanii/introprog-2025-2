#O algoritmo é logicamente funcional, mas pelo fato da necessidade de processar dezenas de milhões de números...
#...o tempo de processamento se torna gigantesco, deixando o algoritmo não funcional na visão prática.
#Pesquisei na web e encontrei uma fórmula para encontrar números perfeitos, e essa se encontra no próximo arquivo.

def main():

    perfeito = []
    num = 2

    while (True):
        soma_divisores = 1

        if (len(perfeito) == 5):
            break

        for i in range(2, num):
            if ((num%i) == 0):
                soma_divisores += i


        if (num == soma_divisores):
            perfeito.append(num)

        num += 1

    print('Números perfeitos:', *perfeito, sep=', ')

main()