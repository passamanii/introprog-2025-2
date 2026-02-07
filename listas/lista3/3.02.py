numbers = []
n = None

def main():
    
    n = int (input ('Informe a quantidade de números à serem inseridos:'))

    for i in range(n):
      
      numbers.append(int (input('Digite o número aqui:')))

    process()

def process():
   
   for i in numbers:
      triple = i * 3
      print(triple)

main()
