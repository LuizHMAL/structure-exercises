# ==============================================================================
# RESUMO COMPLETO: ESTRUTURAS DE DADOS E FUNÇÕES NATIVAS DO PYTHON
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. LISTAS (list), LEN() E RANGE()
# ------------------------------------------------------------------------------
# Listas são mutáveis, ordenadas (mantêm ordem de inserção) e aceitam duplicatas.
lista = [1, 2, 3, 4, 5]
print("Lista original:", lista)

# Forma 1: Iteração direta pelos elementos (mais "Pythônica" e legível)
print("\n--- Iterando diretamente pelos valores ---")
for elemento in lista:
    print(elemento, end=" ")
print()

# Forma 2: Iteração pelos índices usando range() e len()
# len(lista) retorna o tamanho (quantidade de itens) da estrutura -> O(1)
# range(fim) gera números de 0 até (fim - 1)
print("\n--- Iterando pelos índices com range(len()) ---")
for i in range(len(lista)):
    print(f"Índice {i}: valor {lista[i]}")

# Forma 3 (DICA IMPORTANTE): Usando enumerate() para ter índice E valor juntos!
print("\n--- Iterando com enumerate() (Recomendado quando precisa do índice) ---")
for indice, valor in enumerate(lista):
    print(f"Posição {indice} -> {valor}")

# range(inicio, fim, passo):
# - inicio: 10 (inclusivo)
# - fim: 1 (exclusivo, ou seja, para no 2)
# - passo: -1 (decrementando de 1 em 1)
print("\n--- Contagem regressiva com range(10, 1, -1) ---")
for value in range(10, 1, -1):
    print(value, end=" ")
print()


# ------------------------------------------------------------------------------
# 2. FUNÇÕES DE AGREGAÇÃO E ORDENAÇÃO (sum, max, min, sorted)
# ------------------------------------------------------------------------------
print("\n--- Funções Matemáticas e de Agregação ---")
print("Soma de todos os itens (sum):", sum(lista))          # Soma os elementos: 15
print("Maior valor da lista (max):", max(lista))            # Maior elemento: 5
print("Menor valor da lista (min):", min(lista))            # Menor elemento: 1
print("Média dos valores:", sum(lista) / len(lista))        # Média aritmética: 3.0

# sorted() retorna uma NOVA lista ordenada sem alterar a original
lista_baguncada = [5, 1, 4, 2, 3]
print("Ordenada crescente:", sorted(lista_baguncada))
print("Ordenada decrescente:", sorted(lista_baguncada, reverse=True))


# ------------------------------------------------------------------------------
# 3. MÉTODOS DE MANIPULAÇÃO DE LISTAS E INDEXAÇÃO
# ------------------------------------------------------------------------------
print("\n--- Manipulação de Listas ---")

# .append(valor): Adiciona elemento ao FINAL da lista -> Complexidade O(1)
lista.append(6)
print("Após append(6):", lista)

# .insert(indice, valor): Insere em uma posição específica -> Complexidade O(n)
lista.insert(0, 0)  # Insere o 0 no início (índice 0)
print("Após insert(0, 0):", lista)
lista.pop(0)        # Remove o 0 que acabamos de colocar para manter o exemplo

# .pop(indice): Remove e RETORNA o elemento do índice passado.
# Se não passar índice, lista.pop() remove o ÚLTIMO elemento -> O(1)
# Se passar índice no meio/início, ex: lista.pop(1), desloca os demais -> O(n)
removido = lista.pop(1)  # Remove o elemento de índice 1 (que era o número 2)
print(f"Após pop(1) (removeu o {removido}):", lista)

# .remove(valor): Busca e remove a PRIMEIRA ocorrência do valor especificado
# Atenção: Gera ValueError se o valor não existir na lista!
if 4 in lista:
    lista.remove(4)
    print("Após remove(4):", lista)
    lista.insert(2, 4)  # Devolvendo o 4 para a lista

# Indexação Negativa:
# -1 acessa o último elemento, -2 o penúltimo, etc.
print("Último elemento (lista[-1]):", lista[-1])
print("Penúltimo elemento (lista[-2]):", lista[-2])

# Fatiamento (Slicing) -> lista[inicio:fim:passo]
print("Três primeiros elementos (lista[:3]):", lista[:3])
print("Lista invertida com slicing (lista[::-1]):", lista[::-1])


# ------------------------------------------------------------------------------
# 4. MATRIZES (Listas dentro de Listas / Arrays 2D)
# ------------------------------------------------------------------------------
print("\n--- Matrizes (Listas 2D) ---")
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Percorrendo por índices (útil quando precisamos da posição [i][j], ex: diagonal principal)
print("Percorrendo com índices [i][j]:")
for i in range(len(matriz)):              # i percorre as linhas
    for j in range(len(matriz[i])):       # j percorre as colunas da linha i
        print(matriz[i][j], end=" ")
    print()  # Quebra de linha ao final de cada linha da matriz

# Dica: Diagonal principal são os elementos onde i == j (1, 5, 9)
diagonal_principal = [matriz[i][i] for i in range(len(matriz))]
print("Diagonal principal da matriz:", diagonal_principal)


# ------------------------------------------------------------------------------
# 5. TUPLAS (tuple) vs CONJUNTOS (set) - ATENÇÃO À DIFERENÇA!
# ------------------------------------------------------------------------------
print("\n--- Tuplas vs Conjuntos (Sets) ---")

# A) TUPLAS: Usam parênteses () -> São IMUTÁVEIS!
# Uma vez criada, você NÃO pode adicionar, remover ou alterar elementos.
# São mais leves em memória e ótimas para dados fixos (ex: coordenadas, registros).
cidades_tupla = ("São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador")
print("Tupla de cidades:", cidades_tupla)
print("Rio de Janeiro está na tupla?", "Rio de Janeiro" in cidades_tupla)
print("Quantidade de vezes que 'São Paulo' aparece:", cidades_tupla.count("São Paulo"))
print("Índice de 'Belo Horizonte':", cidades_tupla.index("Belo Horizonte"))

# IMPORTANTE: No seu código original, cidades estava com () (tupla), mas chamava
# .add(), .remove() e .discard(). Isso gera erro (AttributeError) em tuplas!
# Esses métodos pertencem aos CONJUNTOS (set), que usam chaves {}!

# B) CONJUNTOS (set): Usam chaves {} -> São MUTÁVEIS, NÃO têm ordem fixa e NÃO aceitam duplicatas!
# A busca (`x in conjunto`) é extremamente rápida: complexidade O(1) (usa tabela hash).
cidades_set = {"São Paulo", "Rio de Janeiro", "Belo Horizonte", "Salvador"}
print("\nConjunto (set) inicial:", cidades_set)

# .add(elemento): Adiciona um item ao conjunto (se já existir, ignora sem duplicar)
cidades_set.add("Brasília")
print("Após add('Brasília'):", cidades_set)

# .remove(elemento): Remove o item, mas GERA ERRO (KeyError) se o item não existir!
cidades_set.remove("Salvador")
print("Após remove('Salvador'):", cidades_set)

# .discard(elemento): Remove o item, mas NÃO gera erro se ele não existir (Mais seguro!)
cidades_set.discard("Salvador")  # "Salvador" já foi removido acima, mas discard não trava o programa!
print("Após discard('Salvador') novamente (sem erro):", cidades_set)

# Operações matemáticas de Conjuntos (Muito cobradas em provas e entrevistas!):
sudeste = {"São Paulo", "Rio de Janeiro", "Belo Horizonte", "Vitória"}
print("União (|):", cidades_set | sudeste)               # Tudo dos dois conjuntos
print("Interseção (&):", cidades_set & sudeste)          # Apenas o que tem em AMBOS
print("Diferença (-):", cidades_set - sudeste)           # O que tem no 1º mas não no 2º


# ------------------------------------------------------------------------------
# 6. DICIONÁRIOS (dict) - CHAVE: VALOR (Essencial!)
# ------------------------------------------------------------------------------
print("\n--- Dicionários (dict) ---")
# Armazenam pares chave: valor. Busca por chave também é O(1).
populacao = {
    "São Paulo": 11450000,
    "Rio de Janeiro": 6211000,
    "Belo Horizonte": 2315000
}

# Acessando e modificando valores
print("População de SP:", populacao["São Paulo"])
populacao["Brasília"] = 2817000  # Adiciona nova chave ou atualiza se já existir

# .get(chave, valor_padrao): Evita erro (KeyError) se a chave não existir!
print("População de Curitiba:", populacao.get("Curitiba", "Não cadastrada"))

# Percorrendo chave e valor com .items()
for cidade, hab in populacao.items():
    print(f"{cidade}: {hab} habitantes")


# ------------------------------------------------------------------------------
# 7. BÔNUS: LIST COMPREHENSION E ZIP()
# ------------------------------------------------------------------------------
print("\n--- List Comprehension e zip() ---")

# List Comprehension: forma concisa de criar listas a partir de outra
# Sintaxe: [expressao for item in iteravel if condicao]
quadrados_pares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print("Quadrados dos números pares de 1 a 10:", quadrados_pares)

# zip(): Combina duas ou mais listas elemento a elemento em pares (tuplas)
nomes = ["Ana", "Bruno", "Carlos"]
notas = [9.5, 8.0, 10.0]
for nome, nota in zip(nomes, notas):
    print(f"Aluno(a) {nome} tirou nota {nota}")