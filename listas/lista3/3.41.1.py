def main():

    soma = 0
    x = int(input('Informe o valor de x:'))
    n = int(input('Informe o valor de n:'))

    for i in range(1, n+1):    
        soma += x*i
    
    print(f'O somatório de {x}*i, de i=1 até i={n} é: {soma}.') 

main()