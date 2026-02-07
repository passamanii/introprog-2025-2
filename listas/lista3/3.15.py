def main():

    while(1):

        calc()

        again = input('Deseja calcular outra potência? Sim(S) ou Não(N):').upper()

        if (again == 'S'):

            continue

        else:

            print('Agradecemos a sua preferência. Obrigado!')

            break

def calc():

    b = int(input('Insira o valor da base:'))
    e = int(input('Insira o valor do expoente:'))

    res = b ** e 

    print(f'O resultado para {b} ** {e} é: {res}.')


main()