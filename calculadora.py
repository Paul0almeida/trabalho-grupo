# === CALCULADORA OPERAÇÕES BÁSICAS DA MATEMÁTICA ===

# Declaracao variaveis
op = 0

# Soma
def somar(num1,num2) :
    calculo = num1 + num2
    print("\nA soma de {} com {} é igual a {}".format(num1,num2,calculo))

# subtração
def sub(num1,num2) :
    calculo = num1 - num2
    print("\nA subtração de {} com {} é igual a {}".format(num1,num2,calculo))

# multiplicação
def multi(num1,num2) :
    calculo = num1 * num2
    print("\nA multiplicação de {} com {} é igual a {}".format(num1,num2,calculo))

# divisão
def dividir(num1,num2) :
    calculo = num1 / num2
    print("\nA divisão de {} com {} é igual a {}".format(num1,num2,calculo))

# campos input 
while True:
    print("=== CALCULADORA OPERAÇÕES BÁSICAS DA MATEMÁTICA ===")
    print ("PRIMA 1 - para somar \nPRIMA 2 - para subtrair \nPRIMA 3 - para multiplicar \nPRIMA 4 - para dividir \nPRIMA 5 - sair ")
    op = int(input("\nINT O NÚMERO DA OPÇÃO: "))  # Convertendo para inteiro
    if op == 5:
        break
    num1 = int(input("\nInt o 1º número: "))  # Convertendo para inteiro
    num2 = int(input("\nInt o 2º número: "))  # Convertendo para inteiro
    if op == 1:
        somar(num1,num2)
    elif op == 2:
        sub(num1,num2)
    elif op == 3:
        multi(num1,num2)
    elif op == 4:
        dividir(num1,num2)
    else:
        print("\n*AVISO* opção inválida")
