def main():

    exp = 0
    produto = 1

    for i in range(92, 1478+1):
        divisores = []
        for j in range(1, i+1):
            if ((i%j) == 0):
                divisores.append(j)
        if (len(divisores) <= 2):
                produto *= i

    while (True):
        if (produto//10):
            produto //= 10
            exp += 1 
        else:
            break
    
    produto_cien = f'{produto} * 10^{exp}'
    print(f'Produto resultante: {produto_cien}.')

main()