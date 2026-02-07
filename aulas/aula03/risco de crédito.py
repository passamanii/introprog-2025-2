idade = int (input ('Insira a sua idade:'))
renda = float (input ('Insira a sua renda mensal:'))
emprego = int (input ('Insira o seu tempo de emprego em anos:'))
divida = float (input ('Insira o somatório das suas dívidas:'))

if (idade < 18):
    print ('INAPTO PARA CRÉDITO.')

else:

    if (renda < 1500):

        if (divida > 1000):
            print ('RISCO ALTO.')
        
        else:
            print ('RISCO BAIXO.')

    