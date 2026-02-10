import random

def main():

    teste1 = []
    teste2 = []

    for i in range(10):

        teste1.append(random.randint(-200,200))

    
    for i in range(len(teste1)):

        if (i % 2 == 0):

            m = teste1[i] * 5
            teste2.append(m)

        else: 

            m = teste1[i] + 5
            teste2.append(m)

    
    print(teste1)
    print(teste2)

main()