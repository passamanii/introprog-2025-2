n = 0 
numbers = []

def main():

    while (1):

        n = int(input('Digite o número aqui:'))
        
        if n < 0:
            break

        numbers.append(n)

    process()


def process():

    k = len(numbers)

    if k == 0:

        print('Nenhum número válido foi digitado.')

    else:

        media = sum(numbers) / k

        print(media)

main()