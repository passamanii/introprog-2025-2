def main():

    n = int(input('Informe o valor de N (1-5):'))

    #Só posso usar if, elif, else.

    if (n == 1):
        F = (1+(1/fatorial(1)))
    elif (n == 2):
        F = (1+(1/fatorial(1))+(1/fatorial(2)))
    elif (n == 3):
        F = (1+(1/fatorial(1))+(1/fatorial(2))+(1/fatorial(3)))
    elif (n == 4):
        F = (1+(1/fatorial(1))+(1/fatorial(2))+(1/fatorial(3))+(1/fatorial(4)))
    elif (n == 5):
        F = (1+(1/fatorial(1))+(1/fatorial(2))+(1/fatorial(3))+(1/fatorial(4))+(1/fatorial(5)))
    else:
        print('Número inválido.')
    
    print(round(F,2))

def fatorial(numero):

    if (numero <= 1):
        return 1
    return numero * fatorial(numero-1) #Usando recursividade :)

def fatorial_alternativo(numero):
    
    fator = 1
    for i in range(1, numero+1):
        fator *= i
    return fator #Usando loop :|

main()