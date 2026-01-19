from collections import deque


def tem_conexao(grafo, inicio, alvo):
    fila = deque([inicio])  # Criamos uma fila com o ponto de partida
    visitados = set()   # Para não entrar em loop inifinito(ciclos!)

    while fila:
        pessoa = fila.popleft()  # Tira p primeiro da fila (FIFO)

        if pessoa == alvo:
            return True  # Encontramos o Charlie!

        if pessoa not in visitados:
            visitados.add(pessoa)
            # Adiciona todos os vizinhos dessa pessoa na fila para investigar depois
            fila.extend(grafo[pessoa])

    return False


# --- Teste ---
rede = {
    "Você": ["Alice", "Bob"],
    "Alice": ["Charlie"],
    "Bob": ["Dani"],
    "Charlie": [],
    "Dani": ["John"],
}

print(f"Existe conexão com o Charlie? {tem_conexao(rede, "Você", "Charlie")}")
