import random

def main():

    A = []
    menores = []

    for i in range(10):

        A.append(random.randint(-10,10))
        
        if (A[i] <= 10):

            menores.append(f'O número na {i + 1}ª posição é: {A[i]}.')

    for i in range(len(menores)):

        print(menores[i])

main()


