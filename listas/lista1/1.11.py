conta = float (input ('Insira o valor da conta do restaurante: '))
gorgeta = float (input ('Insira o valor da gorgeta em porcentagem. Ex: 20. '))
pessoas = float (input ('Insira a quantidade de pessoas para dividir a conta: '))

totalconta = ((conta) + (conta * (gorgeta /100)))
containd = (totalconta / pessoas)

print (f'O valor da conta individual é de: R${(containd):.2f}') #:.2f utilizado para formatar o número com duas casas decimais