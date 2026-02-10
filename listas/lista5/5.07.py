import random

def main():

    E = []

    for i in range(16):

        E.append(random.randint(-20,20))

    print(f'{E}\n')

    for i in range(len(E)):

        temp = E[i]

        if (i <= 7):

            E[i] = E[15 - i]
            E[15 - i] = temp

    print(E)


main()