# Game Número Secreto

num_secreto = 35
numeros = []
tentativas = 10

print("\n******************* Descubra o Número Secreto  *******************")

# definição da estrutura de repetição

while tentativas > 0:

    num = int(input('Digite um número: '))

    if num in numeros:
        print("Ops, você já tentou esse número.")
        continue

    elif num==num_secreto:
        print(f"O número digitado foi: {num}")
        print("Parabéns, você acertou o número oculto!")
        continue

    else:
        if num > num_secreto:
            print(f" Ops, o número oculto é menor que {num}")
        elif num < num_secreto:
            print(f" Ops, o número oculto é maior que {num}")

    numeros.append(num)
    tentativas -= 1

    if tentativas > 0:
        print(f'Você ainda possui {tentativas} tentativas.')
    else:
        print("Suas tentativas acabaram.")

print("Fim de jogo!")
print()

# maior/menor da lista:

print("Número oculto: ", num_secreto)
print("Suas tentativas: ", numeros)
menor = numeros[0]
maior = numeros[0]

for i in numeros:
    if menor > i:
        menor = i
print(f'O menor valor digitado foi {menor}')

for x in numeros:
    if maior < x:
        maior = x
print(f'O maior valor digitado foi {maior}')

