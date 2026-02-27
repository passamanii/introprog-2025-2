def main():

    a, b, c = pede_notas()
    mediaa = calcula_media(a, b, c)
    situacao = verifica_situacao(mediaa)
    print(f'A média das notas do aluno X é: {(mediaa):.2f}.\nEle está {situacao}!')

def pede_notas():

    nota1 = float(input('Informe a 1ª nota do aluno:'))
    nota2 = float(input('Informe a 2ª nota do aluno:'))
    nota3 = float(input('Informe a 3ª nota do aluno:'))

    return nota1, nota2, nota3

def calcula_media(nota1, nota2, nota3):

    media_arit = ((nota1+nota2+nota3) / 3)
    
    return media_arit

def verifica_situacao(media_arit):

    if (media_arit >= 6):
        situacao = 'APROVADO'
    else:
        situacao = 'REPROVADO'
    
    return situacao

main()