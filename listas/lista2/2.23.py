def main():
    
    a, b, c = pede_notas()
    mediaa = calcula_media_arit(a, b, c)
    situacao = verifica_situacao(mediaa)
    print(f'O aluno Fulano de Tal, de média {(mediaa):.2f}, está {situacao}.')

def pede_notas():

    nota1 = float(input('Informe a 1ª nota do aluno:'))
    nota2 = float(input('Informe a 2ª nota do aluno:'))
    nota3 = float(input('Informe a 3ª nota do aluno:'))

    return nota1, nota2, nota3

def calcula_media_arit(nota1, nota2, nota3):

    media_arit = ((nota1+nota2+nota3) / 3)

    return media_arit

def verifica_situacao(media_arit):

    if (media_arit >= 7):
        frase = 'APROVADO'
    elif (media_arit < 5):
        frase = 'REPROVADO'
    else:
        frase = 'DE RECUPERAÇÃO'

    return frase

main()