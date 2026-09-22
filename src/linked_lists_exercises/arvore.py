# g = [[0,0,1,0],
#     [0,0,0,1],
#     [1,0,0,1],
#     [0,1,1,0]]

# print(g)

# print(g[0][3])

# g[0][1] = 1
# g[1][0] = 1

# g = {0: {2}, 1: {3}, 2: {0, 3}, 3: {1, 2}}

# print(3 in g[0])


# g[0].add(1)
# g[1].add(0)

# print(g)



g = [
    [0,1,0,0,0,0],
    [1,0,0,0,0,1],
    [1,0,0,0,1,0],
    [0,1,0,0,1,0],
    [0,0,1,0,0,0],
    [0,0,0,0,0,0]]

print(g)

print(g[0][1])

g = {0: {1}, 1: {0, 5}, 2: {0, 4}, 3: {1, 4}, 4: {2, 3}, 5: {1}}

print(g)

# Matrizes e Grafos Ponderados (Não-direcionado / Bidirecional)
# Se a ligação entre dois nós tem um peso, ele deve ser o mesmo na ida e na volta:
# - Aresta (0, 1): peso 8
# - Aresta (0, 2): peso 7
# - Aresta (1, 3): peso 5
# - Aresta (1, 5): peso 3
# - Aresta (2, 4): peso 9
# - Aresta (3, 4): peso 7

g = [
    [0, 8, 7, 0, 0, 0],  # 0 conecta com 1 (peso 8) e 2 (peso 7)
    [8, 0, 0, 5, 0, 3],  # 1 conecta com 0 (peso 8), 3 (peso 5) e 5 (peso 3)
    [7, 0, 0, 0, 9, 0],  # 2 conecta com 0 (peso 7) e 4 (peso 9)
    [0, 5, 0, 0, 7, 0],  # 3 conecta com 1 (peso 5) e 4 (peso 7)
    [0, 0, 9, 7, 0, 0],  # 4 conecta com 2 (peso 9) e 3 (peso 7)
    [0, 3, 0, 0, 0, 0]   # 5 conecta com 1 (peso 3)
]

print("Matriz ponderada:")
for linha in g:
    print(linha)

print("\nPeso da ligação entre 0 e 1:", g[0][1])

# Dicionário ponderado equivalente:
g = {
    0: {1: 8, 2: 7},
    1: {0: 8, 3: 5, 5: 3},
    2: {0: 7, 4: 9},
    3: {1: 5, 4: 7},
    4: {2: 9, 3: 7},
    5: {1: 3}
}

print("\nDicionário ponderado:")
print(g)
print("Peso de 0 para 1:", g[0][1])