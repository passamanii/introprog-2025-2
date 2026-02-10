def main():

    n1 = float(input('Informe a 1ª nota do aluno:'))
    n2 = float(input('Informe a 2ª nota do aluno:'))
    n3 = float(input('Informe a 3ª nota do aluno:'))

    f = int(input('Informe a quantidade de faltas do aluno:'))

    media = round(MEDIA(n1, n2, n3), 2)

    SITUACAO(media, f)


def MEDIA(numero1, numero2, numero3):

    value = (numero1 + numero2 + numero3) / 3

    return value


def SITUACAO(media_nota, quantidade_faltas):

    if (quantidade_faltas > 18):

        print(f'O aluno está REPROVADO POR FALTAS. Boa sorte no próximo período.\nA média é: {media_nota}')

    elif (media_nota < 6):

        print(f'O aluno está REPROVADO POR NOTA. Boa sorte no próximo período.\nA média é: {media_nota}.')

    else:

        print(f'O aluno está APROVADO POR NOTA! Parabéns pela sua dedicação.\nA média é de: {media_nota}.')


main()