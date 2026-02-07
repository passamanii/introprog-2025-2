num = int (input ('Insira um número inteiro:'))

k = 0

if (num % 10 == 0):
    print ('O número é divisível por 10.')

else:
    k = k + 1


if (num % 5 == 0):
    print ('O número é divisível por 5.')

else:
    k = k + 1


if (num % 2 == 0):
    print ('O número é divisível por 2.')

else:
    k = k + 1


if (k == 3):
    print ('O número não é divisível por nenhum deles (2, 5, 10).')

