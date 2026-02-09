def main():

    odd = []

    for i in range(100, 201):

        if (i % 2 == 1):

            odd.append(i)

    print(f'\nOs números ímpares entre 100 e 200 são:\n\n{odd}')
    

main()