def main():

    base_wage, lcd_sold, plasma_sold = pede_informacoes()
    comission = comission_process(lcd_sold, plasma_sold)
    wage_process(base_wage, comission)

def pede_informacoes():

    salario = float(input('Informe o salário base do funcionário:'))
    lcd = int(input('Informe a quantidade de TVs LCD vendidas:'))
    plasma = int(input('Informe a quantidade de TVs PLASMA vendidas:'))

    return salario, lcd, plasma

def comission_process(lcd, plasma):

    comission = 0

    if (lcd < 10):
        comission += (lcd*5)
    elif (lcd >= 10):
        comission += (lcd*50)
    if (plasma < 20):
        comission += (plasma*2)
    elif (plasma >= 20):
        comission += (plasma*20)
    
    return comission

def wage_process(base_sal, comission):

    pretax_sal = (base_sal + comission)
    inss_discount = (0.08*base_sal)
    ir_discount = 0
    pos_inss_sal = (pretax_sal-inss_discount)
    final_wage: float = pos_inss_sal

    if (pos_inss_sal >= 500):
        ir_discount = (0.15*pos_inss_sal)
        postax_sal = (pos_inss_sal-ir_discount)
        final_wage = postax_sal
    
    print(f'SALÁRIO BASE: R${base_sal}\nCOMISSÃO: R${comission}\nIMPOSTOS: R${round(inss_discount+ir_discount,2)}\nSALÁRIO TOTAL: R${(final_wage):.2f}')

main()