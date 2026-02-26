def main():

    code = int(input('Informe o código do cargo correspondente:'))
    salary = float(input('Informe o sálario do funcionário:'))

    if (code == 101):
        aumento = 0.0
        new_salary = salary + (salary*aumento)
        salary_dif = new_salary - salary
        print(f'Cargo: GERENTE\nSalário antigo: {salary}\nSalário novo: {new_salary}\nDiferença: {salary_dif}')

    elif (code == 102):
        aumento = 0.005
        new_salary = salary + (salary*aumento)
        salary_dif = new_salary - salary
        print(f'Cargo: ANALISTA\nSalário antigo: {salary}\nSalário novo: {new_salary}\nDiferença: {salary_dif}')

    elif (code == 103):
        aumento = 0.015
        new_salary = salary + (salary*aumento)
        salary_dif = new_salary - salary
        print(f'Cargo: PROGRAMADOR\nSalário antigo: {salary}\nSalário novo: {new_salary}\nDiferença: {salary_dif}')

    else:
        aumento = 0.4
        new_salary = salary + (salary*aumento)
        salary_dif = new_salary - salary
        print(f'Cargo: DESCONHECIDO\nSalário antigo: {salary}Salário novo: {new_salary}\nDiferença: {salary_dif}.')
        
main()
    