def main():

    num = int(input('Insira o número desejado:'))

    process(num)


def process(number):

    product = 1
    nums = []

    for i in range(number + 1):

        if i != 0:
            
            product *= i

        nums.append(i)
    
    print(f'Os números são: {nums}.')
    print(f'O produto dos números é: {product}.')


main()