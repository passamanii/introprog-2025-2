def main():

    quantidade = 500
    maior = -9999999999
    menor = 9999999999
    soma = 0

    for i in range(quantidade):

        while (True):
            try:
                temp_num = int(input(f'Informe o {i+1}º número:'))
                break
            except ValueError as error:
                print('Erro:', error)
                continue

        soma += temp_num
        if (temp_num < menor):
             menor = temp_num
        if (temp_num > maior):
            maior = temp_num

    media = (soma/quantidade)

    print(f'MAIOR NÚMERO: {maior}\nMENOR NÚMERO: {menor}\nMÉDIA: {media}')    

main()


