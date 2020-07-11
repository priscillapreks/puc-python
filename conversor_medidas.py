"""
Inteligência Artificial Aplicada (PUC/PR)
Disciplina: Raciocício Algorítmico
Priscilla Bomfim Domingues
"""

ano_luz = {"pc": 0.31,
           "al": 1,
           "ae": 63241.09,
           "ml": 525960.23,
           "sl": 31557609.92
           }

unidades = ["Parsec (pc)",
            "Ano-Luz (al)",
            "Unidade Astronômica (ae)",
            "Minuto-Luz (ml)",
            "Segundo-Luz (sl)"
            ]


def conversor(valor, unid1, unid2):

    valor = float(valor)
    unid1 = ano_luz[unidade_origem]
    unid2 = ano_luz[unidade_destino]

    valor_final = valor * unid1 * unid2
    print(f'\nConversão: {valor} {unidade_origem} = {valor_final} {unidade_destino}')


# Imprime a lista de unidades de conversão

print('**** Conversor ****\n')
for i in unidades:
    print(i)
print(' --- ')

# Solicita valor e unidades

while True:

    valor = input('Valor a ser convertido: ')
    unidade_origem = input('Converter de (sigla): ')
    unidade_destino = input('Converter para (sigla): ')

    # Chama função e exibe o valor convertido
    conversor(valor, unidade_origem, unidade_destino)

    # Sair ou continuar
    continuar = input('\nDeseja fazer outra conversão? (s/n)')

    if continuar is 's':
        continue
    else:
        break
