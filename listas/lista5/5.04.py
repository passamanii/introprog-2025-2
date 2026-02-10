import random

def main():
     
    menor = 9999999999
    p = None
    N = []

    for i in range(20):

        N.append(random.randint(-20,20))

        if (N[i] < menor):
            
            menor = N[i]
            p = i

    print(N)
    print(f'O menor elemento é o de posição {p}, de valor {menor}.')

main()