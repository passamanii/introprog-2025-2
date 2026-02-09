def main():
    
    prod = 1 

    while (1):

        num = float(input('Digite o número desejado:'))

        if (num == 0):
            
            break

        elif (num % 2 == 0):

            prod *= num

        else:

            continue

    
    print(f'O produto dos números pares digitados é: {round(prod)}.')



main()