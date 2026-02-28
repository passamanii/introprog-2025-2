def main():

    a, b = solicita_valores()
    type = verificar_multiplos(a, b)
    print(f'Os números {a} e {b} {type} múltiplos!')

def solicita_valores():
    
    numero1 = int(input('Informe o primeiro número:'))
    numero2 = int(input('Informe o segundo número:'))

    return numero1, numero2

def verificar_multiplos(numero1, numero2):

    if (numero1 >= numero2):
        if (numero1 % numero2 == 0):
            x = 'são'
        else:
            x = 'não são'

    elif (numero2 >= numero1):
        if (numero2 % numero1 == 0):
            x = 'são'
        else:
            x = 'não são'

    return x

main()