n = None

def main():

    n = int(input('Insira a quantidade de números à serem informados:'))

    for i in range(n):

        temp_num = int(input('Digite o número aqui:'))

        if (temp_num <= 0):
            print(f'O número {temp_num} é negativo!')

        else:
            print(f'O número {temp_num} é positivo!')


main()