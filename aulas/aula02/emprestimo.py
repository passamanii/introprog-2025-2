prestacao = float (input ('Informe o valor da prestação:'))
salBruto = float (input ('Informe o seu salário bruto:'))
emprestimoMax = salBruto * 0.3

if ((salBruto * 0.3) < prestacao):
    print ('O empréstimo NÂO PODE ser concedido')

else:
    print ('O empréstimo PODE ser concedido!')

print ('O empréstimo máximo permitido é de: R$',emprestimoMax)
