n = None
numbers = []

def main():

    n = int (input('Informe a quantidade de números à serem inseridos:'))

    while (n < 3):

        n = int (input('Erro. Informe a quantidade de números à serem inseridos (maior/igual à 3):'))

    for i in range(n):

        numbers.append(int(input('Digite o número aqui:')))

    process()


def process():

    k = len(numbers)

    numbers.pop(k-1)
    numbers.pop(0)

    k = len(numbers)

    media = sum(numbers) / k

    print(f'A média excluindo os números extremos é de: {media}')

main()