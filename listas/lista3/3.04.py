neg_numbers = []
n = None

def main():

    n = int(input('Informe a quantidade de números à serem digitados:'))

    for i in range(n):

        temp_num = int(input('Digite o número aqui:'))

        if (temp_num < 0):

            neg_numbers.append(temp_num)

    neg = len(neg_numbers)

    print(f'A quantidade de números negativos informados foi de {neg}.')

main()