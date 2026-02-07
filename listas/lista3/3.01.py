numbers = []
odd_numbers = []
v3odd_numbers = []

def main():


    n1 = int (input ('Insira o primeiro valor:'))
    n2 = int (input ('Insira o segundo valor:'))

    process(n1, n2)
    printar()

def process(x,y):
    
    interval = y - x + 1

    for i in range(interval):
        n = x + i
        numbers.append(n)

        if (n % 2 == 1):
            odd_numbers.append(n)

            if (n % 3 == 0):
                v3odd_numbers.append(n)


def printar():

    print(f'Esses são todos os números do intervalo dado: {numbers}')
    print(f'Esses são todos os números ímpares presentes no intervalo: {odd_numbers}')
    print(f'Esses são todos os números ímpares múltiplos de 3: {v3odd_numbers}')
    


main()