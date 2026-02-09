def main():

    n = 0
    p = 0
    biggest_sal = 0
    soma_sal = 0
    soma_son = 0

    while (1):

        print(f'Cadastro Pessoa {n+1}')

        temp_sal = float(input('Informe o salário aqui:'))
       
        if (temp_sal < 0):
            break

        temp_son = float(input('Informe a quantidade de filhos:'))


        n += 1
        soma_sal += temp_sal
        soma_son += temp_son 

        if (temp_sal > biggest_sal):

            biggest_sal = temp_sal

        if (temp_sal <= 100):

            p += 1

    media_sal = soma_sal / n
    media_son = soma_son / n
    poorpercent = (p/n) * 100

    print(f'O maior salário é: R${(biggest_sal):.2f}.')
    print(f'A média de salários é: R${(media_sal):.2f}.')
    print(f'A média de filhos é: {(media_son):.2f}.')
    print(f'O percentual de pessoas com salário de até R$100 é: {(poorpercent):.2f}%.')


main()