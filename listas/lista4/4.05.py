def main():
    
    k = 0

    while (1):

        name = input(f'Informe o nome do {k + 1}º aluno:').upper()

        if (name == 'FIM'):

            print('Programa encerrado.')
            break
    
        n1 = float(input(f'Informe a primeira nota do {k + 1}º aluno:'))
        n2 = float(input(f'Informe a segunda nota do {k + 1}º aluno:'))
        n3 = float(input(f'Informe a terceira nota do {k + 1}º aluno:'))

        k += 1
        media = MEDIA(n1, n2, n3)

        print(f'A média do aluno {name} é: {(media):.2f}')

def MEDIA(num1, num2, num3):

    value = (num1 + num2 + num3) / 3

    return value


main()