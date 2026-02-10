import random
    
def main():

    P = []
    I = []
    even = 0
    odd = 0

    for i in range(30):

        x = random.randint(-200, 200)

        if (x % 2 == 0):

            if (len(P) < 10):

                P.append(x)
            
            else:

                even += 1
                print(f'{even}º Números pares: {P}.')
                P = []
                P.append(x)

        else:

            if (len(I) < 10):

                I.append(x)

            else:

                odd += 1
                print(f'{odd}º Números ímpares: {I}.')
                I = []
                I.append(x)

    print(f'Números pares restantes: {P}.')
    print(f'Números ímpares restantes: {I}.')


main()