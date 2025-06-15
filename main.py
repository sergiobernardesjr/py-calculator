def sum(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def split(n1, n2):
  return n1 / n2

def mult(n1, n2):
  return n1 * n2

while True:

  op = input("Digite a operação desejada ou 'sair' para sair: ").strip().lower()
  
  if op == 'sair':
    break
 
  n1 = float(input("Digite um número: "))
  n2 = float(input("Digite outro número: "))

  if op == '/':
    resultado = split(n1,n2)

  if op == '-':
    resultado = sub(n1,n2)

  if op == '+':
    resultado = sum(n1,n2)

  if op == '*':
    resultado = mult(n1,n2)



  print(f'Resultado {str(resultado)}')