def main():

    num = int(input('Informe um número de 4 dígitos:'))

    x = (num % 100)
    y = (num // 100)
    z = x + y

    print(f'X: {x}, Y: {y}, Z: {z}.')
    if ((z**2) == num):
        print(f'O número atende os requisitos.')
    else:
        print(f'O número não cumpre nenhum requisito.')

main()