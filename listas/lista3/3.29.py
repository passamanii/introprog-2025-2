def main():

    media = 0
    soma = 0
    pos = 0 
    neg = 0
    neg_percent = 0
    pos_percent = 0
    quant = 0

    quant = int(input('Informe a quantidade de números à serem digitados:'))

    for i in range(quant):

        temp_n = float(input('Digite o número aqui:'))

        if (temp_n >= 0):

            pos += 1

        elif (temp_n < 0):

            neg += 1

        soma += temp_n

    media = soma / quant
    neg_percent = neg/quant * 100
    pos_percent = pos/quant * 100

    print(f'A média aritmética dos números informados é de: {(media):.2f}.')
    print(f'A quantidade de números positivos informados é de: {(pos):.2f}.')
    print(f'A porcentagem de números positivos é de: {(pos_percent):.2f}%.\n')
    print(f'A quantidade de números negativos informados é de: {(neg):.2f}.')
    print(f'A porcentagem de números negativos informados é de: {(neg_percent):.2f}%.')


main()