def main():
    
    divisores = []
    
    while (True):
        try:
            num = int(input('Informe o número desejado:'))
            break
        except ValueError as error:
            print(f'Erro: {error}')
            continue

    for i in range(1, num+1):
        if ((num%i) == 0):
            divisores.append(i)
    
    if (len(divisores) <= 2):
        print(f'O número {num} é primo.')
    else:
        print(f'O número {num} possui os divisores:')
        print(*divisores, sep=', ') #*divisores --> desempacota a lista [X, X] no formato X X. sep=', ' --> coloca ', ' como separador entre os 
                                    # números desempacotados no formato X, X. 
        
main()