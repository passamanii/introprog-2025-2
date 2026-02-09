def main():

    x = float(input('Informe o valor de x:'))
    y = float(input('Informe o valor de y:'))

    print(f'ANTES DA TROCA: X - {x}, Y - {y}.')
    
    x, y = TROCA(x, y)

    print(f'DEPOIS DA TROCA: X - {x}, Y - {y}.')



def TROCA(number1, number2):

    temp = number1

    number1 = number2
    number2 = temp

    return number1, number2


main()