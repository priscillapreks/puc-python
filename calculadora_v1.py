
# Calculadora em Python

print("\n******************* Calculadora Python  *******************")

print('Selecione o número da operação desejada:')

print('1 - Soma', '2 - Subtração', '3 - Multiplicação', '4 - Divisão')

operacao = input("Digite a opção: 1/2/3/4: ")

if operacao == '1':
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    soma = int(num1) + int(num2)
    print("O resultado é: ", soma)

elif operacao == '2':
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    subt = int(num1) - int(num2)
    print("O resultado é: ", subt)

elif operacao == '3':
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    multip = int(num1) * int(num2)
    print("O resultado é: ", multip)

elif operacao == '4':
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    divisao = int(num1) / int(num2)
    print("O resultado é: ", divisao)

else:
    print("oops, escolha uma operação válida")
