def main():

    maior_altura = -999999999
    menor_altura = 999999999
    soma_f = 0 
    soma_t = 0
    f = 0
    q = 3

    for i in range(q):

        sexo, altura = input('Informe o sexo da pessoa, e a altura, no formato (M/F, XXXcm):').split(',')
        altura = int(altura)
        sexo = sexo.upper()

        if (altura < menor_altura):
            menor_altura = altura
        if (altura > maior_altura):
            maior_altura = altura
        if (sexo == 'F'):
            soma_f += altura
            f += 1
        soma_t += altura
    
    media_t = round(soma_t/q, 2)
    media_f = round(soma_f/f, 2)
    print(f'MAIOR ALTURA DA TURMA: {maior_altura}cm\nMENOR ALTURA DA TURMA: {menor_altura}cm\nMÉDIA TOTAL: {media_t}cm\nMÉDIA FEMININA: {media_f}cm')

main()