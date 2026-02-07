lastndono = 0
lastnpet = 0
lasttipopet = 0
lastpesopet = 0
lastvalconsulta = 0

menu = 0
k = 0

valortotal = 0
totalcat = 0
totaldog = 0
totaloutro = 0

while (menu != 4):

    menu = int (input ('Insira a ação desejada: \n"1" - Cadastrar um atendimento \n"2" - Visualizar o último atendimento cadastrado \n"3" - Mostrar estatísticas do dia \n"4" - Fechar programa \nDigite aqui:'))

    while (menu <= 0 or menu > 4):

        print ('Opção inválida! Tente novamente.')
        menu = int (input ('Insira a ação desejada: \n"1" - Cadastrar um atendimento \n"2" - Visualizar o último atendimento cadastrado \n"3" - Mostrar estatísticas do dia \n"4" - Fechar programa \nDigite aqui:'))
    

    if (menu == 1):

        ndono = input ('Informe o nome do dono:')
        npet = input ('Informe o nome do animal:')
        tipopet = int (input (f'Informe o tipo do animal: \n"1" - Cachorro \n"2" - Gato \n"3" - Outro \nDigite aqui:'))

        while (tipopet <= 0 or tipopet > 3):
            print ('Opção inválida! Tente novamente.')
            tipopet = int (input (f'Informe o tipo do animal: \n"1" - Cachorro \n"2" - Gato \n"3" - Outro \nDigite aqui:'))

        pesopet = float (input ('Informe o peso do animal (em KG):'))
        valconsulta = 0

        if (tipopet == 1 and pesopet <= 10):

            valconsulta = 60

        elif (tipopet == 1 and pesopet > 10):

            valconsulta = 80

        elif (tipopet == 2 and pesopet <= 5):

            valconsulta = 50

        elif (tipopet == 2 and pesopet >5):

            valconsulta = 70

        elif (tipopet == 3):

            valconsulta = 90



        conf = input (f'O valor da consulta será de: R${valconsulta}. Confirmar o cadastro? (S/N)') .upper()

        if (conf == "S"):
            
            print ('Cadastro confirmado!')

            lastndono = ndono
            lastnpet = npet 
            lasttipopet = tipopet
            lastpesopet = pesopet
            lastvalconsulta = valconsulta

            k += 1
            valortotal += valconsulta

            if (tipopet == 1):

                totaldog += 1

            elif (tipopet == 2):

                totalcat += 1

            else:

                totaloutro += 1

        else:

            print ('Cadastro cancelado!')

    

    if (menu == 2):

        if (k > 0):

            print ('O último cadastro realizado foi:')

            print (f'Nome do dono: {lastndono}')
            print (f'Nome do animal: {lastnpet}')

            if (lasttipopet == 1):
                print ('Tipo de animal: Cachorro')

            elif (lasttipopet == 2):
                print ('Tipo de animal: Gato')

            else:
                print ('Tipo de animal: Outro')

            print (f'Peso do animal: {lastpesopet}kg')
            print (f'Valor da consulta: R${lastvalconsulta}')

        else:

            print ('Nenhum atendimento foi cadastrado.')

    
    if (menu == 3):

        if (k > 0):

            if (k > 1):

                print (f'Hoje foram realizados {k} atendimentos.')

            else:
                print (f'Hoje foi realizado {k} atendimento.')

        else:
            print ('Não foram realizados cadastros hoje.')


        print (f'O total arrecadado foi de: R${valortotal}')

        print (f'{totaldog} cachorro(s), {totalcat} gato(s) e {totaloutro} outro(s) foram atendidos.')

    
    if (menu == 4):
        
        print ('Obrigado pela preferênia. Volte sempre!')