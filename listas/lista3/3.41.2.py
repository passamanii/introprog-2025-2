def main():

    soma = 0
    x = int(input('Informe o valor de x:'))
    y = int(input('Informe o valor de y:'))
    n = int(input('Informe o valor de n:'))

    for i in range(1, n+1):
        soma += ((x*i)*(y*i))

    print(f'O somatório de {x}, iterando (1->{n}) é: {soma}.')
    
main()
    