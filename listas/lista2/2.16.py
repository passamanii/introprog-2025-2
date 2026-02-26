def main():

    a = float(input('Informe o 1º valor:'))
    b = float(input('Informe o 2º valor:'))
    c = float(input('Informe o 3º valor:'))

    #A é o maior valor
    if (a > b and a > c):
        media = ((a*5) + (b*2.5) + (c*2.5)) / 10
        print(f'A média ponderada dos valores {a}, {b} e {c} é: {(media):.2f}')

    #B é o maior valor
    elif (b > a and b > c):
        media = ((a*2.5) + (b*5) + (c*2.5)) / 10
        print(f'A média ponderada dos valores {a}, {b} e {c} é: {(media):.2f}')

    #C é o maior valor
    else:
        media = ((a*2.5) + (b*2.5) + (c*5)) / 10
        print(f'A média ponderada dos valores {a}, {b} e {c} é: {(media):.2f}')

main()