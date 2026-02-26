def main():

    base_txt = 'Classificação da pessoa: '
    age = int(input('Informe a idade da pessoa aqui:'))

    if (0 <= age <= 18):
        class_txt = 'Menor de Idade.'

    elif (19 <= age <= 64):
        class_txt = 'Maior de Idade.'

    elif (65 <= age):
        class_txt = 'Idosa.'

    print(base_txt + class_txt)

main()