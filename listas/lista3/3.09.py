n = None
numbers = []

def main():
    
    x = int(input('Insira o número desejado:'))
    n = int(input('Informe a quantidade de números à serem lidos:'))

    for i in range(n):

        numbers.append(int(input('Digite o número aqui:')))

    process(x)

def process(x):

    pos = 0

    for i in numbers:
    
        if (i == x):

            shown = 1
            
            break

        else:

            shown = 0
            pos += 1

    if (shown):

        print(f'O número {x} aparece na posição {pos}.')

    else:

        print(f'O número {x} NÂO aparece na lista.')

main()