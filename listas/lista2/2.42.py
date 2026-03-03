def main():

    x = float(input('Informe o valor de x para a equação:'))
    calcula_equacao(x)

def calcula_equacao(valor):

    if (valor <= 1):
        fx = 1
    elif (valor <=2):
        fx = 2
    elif (valor <= 3):
        fx = (valor**2)
    else:
        fx = (valor**3)
    
    print(f'O resultado da equação, com x = {valor}, é: {fx}.')

main()