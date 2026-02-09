def main():

    k = 0
    q = int(input('Informe a quantidade de números à serem inseridos na tabela:'))

    for i in range(q):

        n = float(input('Digite o número à ser inserido aqui:'))

        if (k == 0):

            print(f'|---Número---Quadrado---Cubo---Raiz---|')

        k += 1

        square = (n ** 2)
        cube = (n ** 3)
        root = (n ** (1/2))

        print (f'|---{n}---{square}---{cube}---{root}---|')

        if (k == 19):

            k = 0


main()

            
