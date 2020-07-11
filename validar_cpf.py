# Validador de CPF (Python Básico)

# Loop infinito

while True:

# cpf 39763976014

    cpf = input('Digite um CPF: ')

    new_cpf = cpf[:-2]
    reverse = 10
    total = 0

# Loop do CPF

    for i in range(19):
        if i > 8:
            i -= 9

        total += int(new_cpf[i]) * reverse

        reverse -= 1
        if reverse < 2:
            reverse = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            new_cpf += str(d)

        # Evitar sequencias. Ex.: 11111111111, 00000000000...
        sequencia = new_cpf == str(new_cpf[0]) * len(cpf)

    if cpf == new_cpf and not sequencia:
        print('CPF válido.')

    else:
        print('CPF inválido.')
