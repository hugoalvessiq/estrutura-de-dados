# --- 1. ORDENAÇÃO (Quick Sort) ---
def quick_sort(lista):
    if len(lista) <= 1:
        return lista  # Caso Base: lista vazia ou com 1 item já está ordenada

    pivo = lista[len(lista) // 2]  # Escolhemos o elemento central como pivô
    esquerda = [x for x in lista if x < pivo]   # Menores que o pivô
    meio = [x for x in lista if x == pivo]     # Iguais ao pivô
    direita = [x for x in lista if x > pivo]    # Maiores que o pivô

    # Recursão: ordena os lados e junta tudo
    return quick_sort(esquerda) + meio + quick_sort(direita)

# --- 2. BUSCA (Busca Binária) ---


def busca_binaria(lista, alvo):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == alvo:
            return meio  # Encontrou! Retorna a posição
        if chute > alvo:
            alto = meio - 1  # Alvo está na esquerda
        else:
            baixo = meio + 1  # Alvo está na direita
    return None  # Não encontrou


# --- TESTANDO TUDO ---
ids_livros = [40, 10, 70, 30, 60, 20, 50]
print(f"IDs originais: {ids_livros}")

ids_livros.insert(-1, 40)
print(f"Lista Livros: {ids_livros}")
# Passo 1: Ordenar (essencial para a busca binária)
ids_ordenados = quick_sort(ids_livros)
print(f"IDs ordenados: {ids_ordenados}")

# Passo 2: Buscar o livro com ID 60
posicao = busca_binaria(ids_ordenados, 60)
print(f"O livro 60 está na posição: {posicao}")

# Passo 3: Buscar o livro com ID 40
posicao = busca_binaria(ids_ordenados, 40)
print(f"O livro 40 está na posição: {posicao}")
