def main():

    soma = 0 
    x = int(input('Informe o valor de x:'))
    n = int(input('Informe o valor de n:'))

    for i in range(1, n+1):
        soma += ((x*i)**2)

    print(f'O somatório de {x}, iterando de 1 à {n} é: {soma}.')

main()