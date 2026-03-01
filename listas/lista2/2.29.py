def main():
    
    media = float(input('Informe a média do aluno na disciplina:'))
    conceito = vef_condicao(media)
    print(f'A condição do aluno Fulaninho de Souza, de média {media} é {conceito}.')

def vef_condicao(media_final):

    if (media_final < 5):
        grade = 'D'
    elif (media_final < 7):
        grade = 'C'
    elif (media_final < 9):
        grade = 'B'
    else:
        grade = 'A'
    return grade
    
main()
