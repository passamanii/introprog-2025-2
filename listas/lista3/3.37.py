def main():

    quantidade = 3
    biggest = -9999999999
    big_num = None
    smallest = 9999999999
    smol_num = None

    for i in range(quantidade):

        while(True):
            try:
                student_number, student_height = input(f'Insira o número do {i+1}º aluno e sua altura correspondente, no formato (XXXX, X.XX):').split(',')
                student_height = float(student_height)
                break 

            except ValueError as error:
                print('Erro:', error)
                continue
        
        if (student_height < smallest):
            smallest = student_height
            smol_num = student_number
        if (student_height > biggest):
            biggest = student_height
            big_num = student_number

    print(f'---ALUNO MAIS ALTO---\nCÓDIGO: {big_num}\nALTURA: {biggest}m\n\n---ALUNO MAIS BAIXO---\nCÓDIGO: {smol_num}\nALTURA: {smallest}m')

main()