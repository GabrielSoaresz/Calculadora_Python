#Calculadora com while

while True:
    num1 = (input("Digite um número: "))
    num2 = (input("Digite outro número: "))
    operador = input("Digite um operador (+,-,*,/):")

    numeros_validos = None
    num1_float = 0
    num2_float = 0
    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = "+-*/"

    if operador not in operadores_permitidos:
        print("Operador inválido.")
        continue
    
    if len(operador) > 1:
        print("digite apenas um operador.")
        continue
    
    if operador == '+':
        print(f'{num1} + {num2} =',num1_float + num2_float)
    elif operador == '-':
        print(f'{num1} - {num2} =',num1_float - num2_float)
    elif operador == '*':
        print(f'{num1} * {num2} =',num1_float * num2_float)
    elif operador == '/':
        print(f'{num1} / {num2} =',num1_float / num2_float)
    else:
        print("Nunca deveria ter chegado aqui")    

    sair = input('Quer sair? [s]im: ').lower().startswith('s') #startswith -> Tipo booleano que retorna True ou False se a string começar com o valor especificado.

    if sair is True:
        break