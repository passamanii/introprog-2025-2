def main():

    odd = 0
    even = 0
    q = 0
    media_even = 0 
    soma_even = 0
    media_all = 0
    soma_all = 0


    while (1):

        n = int(input('Digite o número aqui:'))

        if (n == 0):

            print(f'Programa encerrado.')
            break

        if (n % 2 == 0):

            even += 1
            soma_even += n
        

        elif (n % 2 == 1):

            odd += 1
        
        soma_all += n
        q += 1

    if (even > 0):

        media_even = soma_even / q

    media_all = soma_all / q
        

    print(f'A média dos números informados é de: {(media_all):.2f}.')
    print(f'\nA média dos números pares informados é de: {(media_even):.2f}.')
    
    if (even > 0):

        print(f'A quantidade de números pares informados é: {(even):.2f}.')

    else:

        print(f'Não foram informados números pares.')

    if (odd > 0):

        print(f'A quantidade de números ímpares informados é: {(odd):.2f}.')

    else:

        print(f'Não foram informados números ímpares.')



main()

