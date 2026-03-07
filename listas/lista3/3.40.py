def main():

    especimes = 0
    maior_idade = -999999999
    q = int(input('Informe a quantidade de pessoas à serem entrevistadas:'))

    for i in range(q):
        sexo = input(f'Informe o sexo da {i+1}ª pessoa (M/F):').upper()
        cor_olho = input(f'Informe a cor dos olhos (AZUL/VERDE/CASTANHO):').upper()
        cor_cabelo = input(f'Informe a cor do cabelo (LOURO/CASTANHO/PRETO):').upper()
        idade = int(input('Informe a idade:'))

        if (idade > maior_idade):
            maior_idade = idade
        if ((sexo == 'F') and (18 <= idade <= 35) and (cor_olho == 'VERDE') and (cor_cabelo == 'LOURO')):
            especimes += 1

    print(f'MAIOR IDADE DOS HABITANTES: {maior_idade}\n'
          f'QUANTIDADE DE MULHERES LOURAS, DE OLHOS VERDES, ENTRE 18 E 35 ANOS: {especimes}')

main()