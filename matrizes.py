"""
Inteligência Artificial Aplicada (PUC/PR)
Disciplina: Raciocício Algorítmico
Priscilla Bomfim Domingues
"""

# (a)   implementar um algoritmo que crie uma matriz utilizando listas (lista de listas) com dimensões 3 x 3.
# O programa deve inserir na matriz apenas valores zeros (0) e uns (1). A diagonal dessa matriz deve ser preenchida
# com o valor um (1) e o restante com o valor zero (0). O programa deve também imprimir a matriz depois de sua criação.
#                 E.g.: [ [ 1, 0, 0 ],
#                       [ 0, 1, 0 ],
#                       [ 0, 0, 1 ] ]

m = []
i = 0

for x in range(3):
    m.append([0]*3)
    m[i][i] = 1
    i += 1

print(m)

print()
# b) implementar o mesmo algoritmo para criar uma matriz 3 x 3 utilizando a estrutura de dicionário.
#                 E.g.: { 0: { 0: 1,  1: 0,  2: 0 },
#                         1: { 0: 0,  1: 1,  2: 0 },
#                         2: { 0: 0,  1: 0,  2: 1 }}


m2 = {}

for x in range(3):
    m2[x] = {}
    for y in range(3):
        if x == y:
            m2[x][y] = 1
        else:
            m2[x][y] = 0
print(m2)