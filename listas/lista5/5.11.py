def main():

    A = []
    B = []
    C = []

    for i in range(0, 100, 8):

        A.append(i)

    for i in range(0, 100, 12):

        B.append(i)

    
    for i in A:

        for j in B:

            if (i == j):

                C.append(i)

    print(A)
    print(B)
    print(C)


main()