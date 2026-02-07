nota1 = float (input ('Insira a primeira nota:'))
nota2 = float (input ('Insira a segunda nota:'))
nota3 = float (input ('Insira a terceira nota:'))

media = ((nota1 + nota2 + nota3) / 3)

print (f"A sua nota média foi de: {media:2.1f}") # (f'aaa': {var:.Xf}')

if ((media < 7) and (media >= 5)):
    print ('Recuperação.')

if ((media >=7)):
    print ('Aprovado.')

if ((media <5)):
    print ('Reprovado.')



'''
CÓDIGO OTIMIZADO:

if (media >=7):
    print ('Aprovado.')

else:

    if (media >=5):
        print ('Recuperação.')

    else:

        if (media < 5):
            print ('Reprovado.')

'''