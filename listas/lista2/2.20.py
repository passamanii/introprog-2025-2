def main():
    
    a = int(input('Informe a medida do 1º lado:'))
    b = int(input('Informe a medida do 2º lado:'))
    c = int(input('Informe a medida do 3º lado:'))
   
    if ((a < b+c) and (b < a+c) and ((c < a+b))):
        identificar_tipo_triangulo(a, b, c)

    else:
        print(f'Não é possível formar um triângulo com os lados {a}, {b} e {c}.')


def identificar_tipo_triangulo(lado1, lado2, lado3):
    
    if ((lado1 == lado2) and (lado1 == lado3)):
        print(f'O triângulo formado pelos lados {lado1}, {lado2} e {lado3} é EQUILÁTERO.')
    
    #Poderia simplesmente verificar se os 3 lados são distintos, caso positivo, seria escaleno, caso negativo, só restaria o isósceles. Mas, para fins de 
    #desenvolvimento de lógica, optei por tentar identifcar um triângulo isósceles.

    elif (((lado1 == lado2) and (lado1 != lado3)) or ((lado2 == lado3) and (lado2 != lado1)) or ((lado3 == lado1) and (lado3 != lado2))):
        print(f'O triângulo formado pelos lados {lado1}, {lado2}, e {lado3} é ISÓSCELES.')

    else:
        print(f'O triângulo formado pelos lados {lado1}, {lado2} e {lado3} é ESCALENO.')

main()