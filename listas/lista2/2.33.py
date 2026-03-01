def main():

    peso = float(input('Informe o peso da pessoa aqui:'))
    altura = int(input('Informe a altura em cm aqui:'))

    imc = (peso / ((altura/100)**2))

    if (imc < 18.5):
        condicao = 'abaixo do peso'
    elif (imc < 25):
        condicao = 'com peso normal'
    elif (imc < 30):
        condicao = 'acima do peso'
    elif (imc < 100):
        condicao = 'obeso'
    else:
        condicao = 'do tamanho de um planeta'
    
    print(f'Fulano de Tal está {condicao}.\nIMC = {(imc):.2f}.')

main()