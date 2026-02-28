def main():

    alt = int(input('Informe a altura em centímetros aqui:'))
    sex = input('Informe o sexo aqui (M/F):').upper()
    p_ideal, frase = calculadora_peso_ideal(alt, sex)
    print(f'O peso ideal de {frase} com {alt}cm de altura é: {(p_ideal):.2f}kg.')

def calculadora_peso_ideal(altura, sexo):

    if (sexo == 'M'):
        peso_ideal = ((72.7*(altura/100))-58)
        frase = 'um homem'
    elif (sexo == 'F'):
        peso_ideal = ((62.1*(altura/100))-44.7)
        frase = 'uma mulher'
    else:
        print('Sexo desconhecido.')
    
    return peso_ideal, frase

main()