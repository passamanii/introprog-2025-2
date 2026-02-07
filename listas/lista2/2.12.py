sal = float (input ('Insira o salário bruto do estatutário:'))
prest = float (input ('Insira o valor da prestação:'))

if ((sal * 0.3) >= prest):
    print ('Empréstimo Concedido.')

else:
    print ('Empréstimo Negado.')