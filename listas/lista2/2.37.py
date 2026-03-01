def main():
    
    tipo_de_figura = input('"Q" - Quadrado\n"R" - Retângulo\n"T" - Triângulo\n"P" - Trapézio\nDeseja calcular a área de que tipo de figura? ').upper()


    if (tipo_de_figura == 'Q'):
        figura = 'quadrado'
        lado = float(input('Informe o valor do lado:'))
        area = (lado**2)
    elif (tipo_de_figura == 'R'):
        figura = 'retângulo'
        lado = float(input('Informe a medida do lado:'))
        altura = float(input('Informe a medida da altura:'))
        area = (lado*altura)
    elif (tipo_de_figura == 'T'):
        figura = 'triângulo'
        base = float(input('Informe o valor da base:'))
        altura = float(input('Informe o valor da altura:'))
        area = ((base*altura)/2)
    elif(tipo_de_figura == 'P'):
        figura = 'trapézio'
        base_menor = float(input('Informe a medida da base menor:'))
        base_maior = float(input('Informe a medida da base maior:'))
        altura = float(input('Informe a medida da altura:'))
        area = (((base_menor+base_maior)/2)*altura)

    print(f'A área do {figura} é: {(area):.2f}cm².')

main()