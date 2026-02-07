numbers = []

def main():

    for i in range(5):

        numbers.append(int(input('Digite o número aqui:')))

    process()

def process():

    big = -999999999999999999
    smol = 999999999999999999

    for i in numbers:
        
        if (i > big):
            big = i 

        if (i < smol):
            smol = i

    print(f'O maior número inserido foi: {big}')
    print(f'O menor número inserido foi: {smol}')

main()