def main():
    i0 = 0
    i1 = 25
    i2 = 50
    i3 = 75
    i4 = 100

    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    q = int(input('Informe a quantidade de números à serem inseridos:'))

    for i in range(q):

        n = float(input(f'Digite o {(i + 1)}ª número aqui:'))

        if (n < 0 or n > 100):

            n = float(input('Número inválido.'))
            continue

        elif (n >= i0 and n <= i1):

            q1 += 1

        elif (n > i1 and n <= i2):

            q2 += 1

        elif (n > i2 and n <= i3):

            q3 += 1

        elif (n > i3 and n <= i4):

            q4 += 1

    print(f'No intervalo [0-25] há {q1} números.\nNo intervalo [26-50] há {q2} números.\nNo intervalo [52-75] há {q3} números.\nNo intervalo [76-100] há {q4} números.')

main()