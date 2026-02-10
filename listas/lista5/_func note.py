def functions(numero, indice, start, stop, step, nome, a, b, indiceinicial, indicefinal):

    L = list()
    L = []

    L.append(numero)

    if (numero in L):
        pass

    L.remove(numero)
    L.pop(indice)

    i = 0

    while i < len(L):

        print(L[i])
        i += 1


    for i in range(start, stop, step):
        pass

    for indice, nome in enumerate(L):
        pass


    import random

    random.randint(a, b) #Interval

    random.shuffle(L)

    random.choice(L)

    L.sort() #Imprime em ordem crescente. ALTERA A LISTA!
    
    L.sort(reverse = True) #Imprime em ordem decrescente. ALTERA A LISTA!

    print(sorted(L)) #Imprime em ordem crescente. Só altera o PRINT!
    
    print(reversed(L)) #Imprime em ordem decrescente. Só altera o PRINT!

    L1 = [1, 2]
    L2 = [3, 4]
    L3 = L1 + L2 # L3 = [1, 2, 3, 4]

    L1 = []
    L2 = [1, 2, 3, 4, 5, 6]
    L1 += L2 # L1 = [1, 2, 3, 4, 5, 6]

    L1 = [1, 2]
    print(L1*3) #Imprime [1, 2, 1, 2, 1, 2]

    L = []
    x = input('Informe o valor:')
    L += [x] #Adiciona o valor do input na lista

    L = []
    x = input('Informe o valor:')
    L.append(x) #Também adiciona o valor do input na lista

    L = [0, 1, 2, 3, 4]
    L[indiceinicial : indicefinal : step]
    print(L[:4]) # [0, 1, 2, 3]


    L = [0, 1]
    V = L #Ambos apontam para o mesmo espaço de armazenamento [0, 1]

    print(L) #[0, 1]
    print(V) #[0, 1]

    L = [0, 1]
    V = L[:]

    print(L) #Aponta para um armazenamento x [0, 1]
    print(V) #Aponta para um armazenamento y [0, 1]


    L = [0, 1, 2]
    V = [3, 4, 5]
    W = [L, V, 6, 7, 8]
    W[0] #É a lista L
    W[1] #É a lista V
    W[2-4] #Sâo os elemntos 6, 7, 8
    # A lista W tem 5 elementos


    L = []

    for i in range(5):

        L.append(i ** 2)

    #L é igual à [0, 1, 4, 9, 16


    