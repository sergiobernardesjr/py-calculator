n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
op = input("Digite a operação desejada: ")

if op == '/':
  resultado = n1/n2

elif op == '-':
  resultado = n1 - n2

elif op == '+':
  resultado = n1 + n2

elif op == '*':
  resultado = n1 * n2

print(f'Resultado {str(resultado)}')