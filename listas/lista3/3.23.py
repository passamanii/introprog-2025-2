def main():

    total_1 = 0
    total_2 = 0
    total_3 = 0
    total_4 = 0
    total_5 = 0
    total_6 = 0
    n = 0

    while (1):

        code = int(input(f'---Candidatos à Melhor Professor---\n0 - Fechar Programa\n1 - Pedro\n2 - Fernando\n3 - Faimison\n4 - Fabiani\n5 - Voto nulo\n6 - Voto em branco\n\nEleitor {n+1}\nInsira o seu voto:'))

        if (code == 0):
            
            break


        elif (code == 1):

            total_1 += 1

        elif (code == 2):

            total_2 += 1

        elif (code == 3):

            total_3 += 1

        elif (code == 4):

            total_4 += 1

        elif (code == 5):

            total_5 += 1

        elif (code == 6):

            total_6 += 1

        n += 1

    if (n == 0):

        print('\nNão houveram votos.')

    else:

        print(f'\nO total de votos para Pedro(1) foi: {total_1}.\nO total de votos para Fernando(2) foi: {total_2}.\nO total de votos para Famison(3) foi: {total_3}.\nO total de votos para Fabiani(4) foi: {total_4}.')
        print(f'O total de votos nulos foi: {total_5}.')
        print(f'O total de votos em branco foi: {total_6}.')


main()



