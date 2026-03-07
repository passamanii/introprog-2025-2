def main():

    soma_sal = 0
    maior_idade = -999
    menor_idade = 999
    mulheres_1000 = 0
    q = 3

    for i in range(q):
        while (True):
            try:
                idade, sexo, sal = input('Informe a idade, sexo e salário, no formato (XX, M/F, XXXX):').split(',')
                sexo = sexo.strip()
                if (sexo != 'm' and sexo != 'M' and sexo != 'F' and sexo != 'f'):
                    raise ValueError('Informe um caracter de sexo válido.')
                break
            except ValueError as error:
                print('Erro:', error)
                continue

        idade = int(idade)
        sal = float(sal)
        soma_sal += sal
        
        if (idade < menor_idade):
            menor_idade = idade
        if (idade > maior_idade):
            maior_idade = idade
        if (sexo == 'F' and sal <= 1000):
            mulheres_1000 += 1
    
    media = round(soma_sal/q)

    print(f'MÉDIA DOS SALÁRIOS: R${media}\n'
          f'MAIOR IDADE: {maior_idade} anos\n'
          f'MENOR IDADE: {menor_idade} anos\n' 
          f'QUANTIDADE DE MULHERES COM MENOS R$1000: {mulheres_1000}')

main()