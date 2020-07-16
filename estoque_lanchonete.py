"""
Inteligência Artificial Aplicada (PUC/PR)
Disciplina: Raciocínio Algorítmico
Priscilla Bomfim
"""

# Estoque de produtos
estoque = {'pao': 10,
           'hamburguer': 12,
           'tomate': 5,
           'bacon': 5,
           'ovo': 5}

# Dic cardápio
cardapio = {'x-burguer': ['pao', 'hamburguer'],
            'x-salada': ['pao', 'hamburguer', 'tomate'],
            'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
            'x-egg': ['pao', 'hamburguer', 'ovo'],
            'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']}


# Verifica ingredientes e atende o pedido
def xburguer(pedido):

    if estoque['pao'] >= 1 and estoque['hamburguer'] >= 1:
        print(f'Um {pedido} saindo no capricho!')

        estoque['pao'] -= 1
        estoque['hamburguer'] -= 1

    else:
        return falta_produto(pedido)


def xsalada(pedido):

    if estoque['pao'] >= 1 and \
            estoque['hamburguer'] >= 1 and \
            estoque['tomate'] >= 1:
        # se todas as condições são verdadeiras, atende o pedido
        print(f'Um {pedido} saindo no capricho!')

        estoque['pao'] -= 1
        estoque['hamburguer'] -= 1
        estoque['tomate'] -= 1

    else:
        return falta_produto(pedido)


def xbacon(pedido):

    if estoque['pao'] >= 1 and \
            estoque['hamburguer'] >= 1 and \
            estoque['tomate'] >= 1 and \
            estoque['bacon'] >= 1:
        # se todas as condições são verdadeiras, atende o pedido
        print(f'Um {pedido} saindo no capricho!')

        estoque['pao'] -= 1
        estoque['hamburguer'] -= 1
        estoque['tomate'] -= 1
        estoque['bacon'] -= 1

    else:
        return falta_produto(pedido)


def xegg(pedido):

    if estoque['pao'] >= 1 and \
            estoque['hamburguer'] >= 1 and \
            estoque['ovo'] >= 1:
        # se todas as condições são verdadeiras, atende o pedido
        print(f'Um {pedido} saindo no capricho!')

        estoque['pao'] -= 1
        estoque['hamburguer'] -= 1
        estoque['ovo'] -= 1

    else:
        return falta_produto(pedido)


def xtudo(pedido):

    if estoque['pao'] >= 1 and \
            estoque['hamburguer'] >= 2 and \
            estoque['tomate'] >= 1 and \
            estoque['bacon'] >= 1 and \
            estoque['ovo'] >= 1:
        # se todas as condições são verdadeiras, atende o pedido
        print(f'Um {pedido} saindo no capricho!')

        estoque['pao'] -= 1
        estoque['hamburguer'] -= 2
        estoque['tomate'] -= 1
        estoque['bacon'] -= 1
        estoque['ovo'] -= 1

    else:
        return falta_produto(pedido)


# Função em caso de ingrediente faltante
def falta_produto(pedido):

    for item in cardapio.get(pedido):
        if estoque[item] > 0:
            pass
        else:
            print(f'Infelizmente acabou o {item}!')


# Imprime o cardápio
for k in cardapio.keys():
    print(k)

# Faz o pedido até que o usuário digite '0' e saia do programa
while True:

    pedido = input('\nO que deseja pedir (0 para sair)? ')

    if pedido == 'x-burguer':
        xburguer(pedido)
    elif pedido == 'x-salada':
        xsalada(pedido)
    elif pedido == 'x-bacon':
        xbacon(pedido)
    elif pedido == 'x-egg':
        xegg(pedido)
    elif pedido == 'x-tudo':
        xtudo(pedido)
    elif pedido == '0':
        break
    else:
        print('Item não localizado no cardápio')
