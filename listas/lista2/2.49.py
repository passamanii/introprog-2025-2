def main():
    
    while (True):

        a = float(input('\nInforme o valor para o coeficiente "a":'))
        b = float(input('Informe o valor para o coeficiente "b":'))
        c = float(input('Informe o valor para o coeficiente "c":'))

        raiz1, raiz2 = calcula_raizes(a, b, c)
        print_raizes(a, b, c, raiz1, raiz2)

        reload = input('\nDeseja calcular mais raízes(S/N)?').upper()

        if (reload == 'N'):
            break

def calcula_raizes(a, b, c):

    delta = ((b**2) - (4*a*c))

    if (delta < 0):
        return None, None
    
    x1 = round(((-(b)+(delta**(1/2))) / (2*a)), 4)
    x2 = round(((-(b)-(delta**(1/2))) / (2*a)), 4)

    return x1, x2

def print_raizes(a, b, c, x1, x2):

    if (x1 == None):
        print('Não existem raízes para os coeficientes dados.')
    else:
        print(f'As raízes da equação do 2º grau de coeficientes {a}, {b}, {c} são: {x1} e {x2}.')

main()
