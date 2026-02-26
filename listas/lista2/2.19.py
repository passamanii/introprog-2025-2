def main():
    
    a = int(input('Informe a medida do lado A:'))
    b = int(input('Informe a medida do lado B:'))
    c = int(input('Informe a medida do lado C:'))

    p = (a + b + c) / 2

    if ((a < b + c) and (b < a + c) and (c < a + b)):    
        area = (p*(p-a)*(p-b)*(p-c)) ** (1/2) #Fórmula de Heron
        print(f'A área do triângulo de lados {a}, {b}, {c} é: {(area):.2f} U.A..')
    
    else:
        print(f'Os lados {a}, {b} e {c} não formam um triângulo.')

main()