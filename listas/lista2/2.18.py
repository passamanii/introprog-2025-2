def main():

    n1 = float(input('Informe a 1ª nota aqui:'))
    n2 = float(input('Informe a 2ª nota aqui:'))
    n3 = float(input('Informe a 3ª nota aqui:'))
    type = input('(A) - Aritmética\n(P) - Ponderada\nInforme o tipo de média desejado:').lower()

    if (type == 'a'):
        media = ((n1 + n2 + n3) / 3)
        print(f'A média aritmética dos números {n1}, {n2}, {n3} é: {media}.')

    elif (type == 'p'):
        media = (((n1*3) + (n2*3) + (n3*4)) / 10)
        print(f'A média ponderada dos números {n1}, {n2}, {n3} é: {media}.')
        
main()