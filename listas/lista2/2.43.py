def main():

    x = float(input('Informe o valor de x para a equação:'))
        
    while (x == 4):
        x = float(input('4 é um número inválido. Informe outro valor para x:'))

    calcula_equacao(x)

def calcula_equacao(v):

    fx = (((5*v)+3)/(((v**2)-16)**(1/2)))
    print(f'O resultado da equação, com x = {v}, é: {(fx):.2f}.')

main()