def main():

    while (True):
        code = int(input('Insira o código do produto:'))

        if ((code != 1001) and (code != 1324) and (code != 6548) and (code != 987) and (code != 7623)):
            code = int(input('Código Inválido.\nInsira o código do produto:'))
        else:
            break
    
    quant = int(input('Informe a quantidade comprada:'))

    if (code == 1001):
        preco = 5.32
    elif (code == 1324):
        preco = 6.45
    elif (code == 6548):
        preco = 2.37
    elif (code == 987):
        preco = 5.32
    else:
        preco = 6.45
    
    total = (preco*quant)
    print(f'O total devido pelo cliente é de R${total}.')

main()