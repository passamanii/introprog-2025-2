def main():

    while (1):

        c = int(input('Informe o código do produto:'))
        p = float(input('Informe o custo atual do produto:'))

        p20 = p * 1.2

        if (p < 0):

            print(f'Programa encerrado.')
            break

        else:

            print(f'|\t\tCódigo\t\tPreço_Antigo\t\tPreço_Novo\t\t|\n|{(c):12}{(p):12}{(p20):12}|')


main()