import time
import sys
import random

# Aumenta o limite de recursão para listas muito grandes (opcional, mas seguro)
sys.setrecursionlimit(2000)


class Node:
    """
    Representa um único nó (elemento) na Lista Ligada.
    Cada nó armazena um valor de dado e um ponteiro para o próximo nó.
    """

    def __init__(self, data):

        # 1. O valor real que o nó armazena.
        self.data = data

        # 2. O ponteiro/link para o próximo nó.
        # Inicialmente é None, pois o nó não aponta para mais nada.
        self.next = None


class LinkedList:
    """
    Classe gerenciadora da Lista Ligada.
    Controla o início (head) e o tamanho (length) da lista.
    """

    def __init__(self):
        # O ponteiro 'head' aponta para o PRIMEIRO nó da lista.
        # Se a lista estiver vazia, head é None.
        self.head = None

        # Ponteiro opcional para o ÚLTIMO nó. Útil para operações rápidas no final.
        self.tail = None

        # Contador do número de nós na lista.
        self.length = 0

    def append(self, data):
        new_node = Node(data)

        # Cenário 1: Lista Vazia
        if self.head is None:
            # Novo nó é o primeiro e o último
            self.head = new_node
            self.tail = new_node

            # Cenário 2: Lista Não Vazia
        else:
            # O último nó atual (tail) precisa apontar para o novo nó
            self.tail.next = new_node

            # O novo nó se torna o novo tail
            self.tail = new_node

        self.length += 1

    def prepend(self, data):
        new_node = Node(data)

        # 1. Faça o next do novo nó apontar para o nó que é a HEAD 		atual.
        #    Se a lista estiver vazia, new_node.next aponta para None (		que é self.head).
        #    Isso funciona para ambos os casos.
        new_node.next = self.head

        # 2. Se a lista estava vazia ANTES da operação, o novo nó é o 		tail também.
        if self.head is None:
            self.tail = new_node

        # 3. Atualize o head para ser o novo nó.
        #    Esta é a única alteração necessária no head.
        self.head = new_node

        self.length += 1

    def insertAt(self, index, data):
        # 1. Checagens de Segurança/Otmização (0(1))

        # Caso 1 Index inválido (não negativo além do tamanho)
        if index < 0 or index > self.length:
            print("Erro: Índice fora dos limites")
            return

        # Caso 2: Inserir no Início (index = 0)
        if index == 0:
            self.prepend(data)
            return

        # Caso 3: Inserir no Final (index = self.length)
        if index == self.length:
            self.append(data)

        # 2. Inserção no Meio (Travessia O(n))
        new_node = Node(data)

        # Encontra o nó LÍDER (o nó ANTERIOR ao ponto de inserção)
        # Devemos parar no índice (index - 1)
        leader = self.head
        count = 0

        while count < index - 1:
            leader = leader.next
            count += 1

        # O nó 'leader' está agora na posição 'index - 1'

        # 3. Manipulação de Ponteiros (0(1)) após a travessia):

        # O novo nó (new_node) deve herdar a conexão do leader.
        # Ou seja, new_node aponta para o nó que o leader apontava antes
        new_node.next = leader.next

        # O leader deve agora apontar para o novo nó
        leader.next = new_node

        self.length += 1

    def removeAt(self, index):
        # 1. Checagens de Segurança/Otimização (O(1)):
        # Índices válidos: 0 até length - 1
        if index < 0 or index >= self.length:
            print("Erro: Índice fora dos limites.")
            return

        # Caso especial 1: Remoção da HEAD (index = 0)
        if index == 0:
            # self.head avança para o próximo nó. O nó original será coletado pelo Python.
            self.head = self.head.next

            # Se a lista ficou vazia, o tail deve ser None.
            if self.head is None:
                self.tail = None

            self.length -= 1
            return  # Termina aqui

        # 2. Travessia para remoção no Meio/Fim (O(n)):
        leader = self.head
        count = 0

        # Percorre até o nó ANTERIOR ao que será removido (índice index - 1)
        while count < index - 1:
            leader = leader.next
            count += 1

        # O nó 'unwanted' é o alvo da remoção
        unwanted = leader.next

        # 3. Manipulação de Ponteiros (O(1) - Pular o nó):
        # O 'leader' agora aponta para o nó após o 'unwanted', removendo-o logicamente.
        leader.next = unwanted.next

        # 4. Caso Especial 2: Atualização do TAIL (O(1)):
        # Se o nó removido era o último, o leader é o novo tail.
        if unwanted == self.tail:
            self.tail = leader

        self.length -= 1

        # Retornar o dado removido pode ser útil (opcional)
        return unwanted.data

    def printList(self):
        # Onde a travessia começa?
        current_node = self.head

        # Variável para construir a saída (ex: '10 -> 20 -> 30 -> None')
        output = ""

        # Loop enquanto houver um nó para visitar
        while current_node is not None:
            # 1. Adicione o dado do nó atual à saída
            output += str(current_node.data) + " -> "

            # 2. Mova-se para o próximo nó
            current_node = current_node.next

        output += "None"

        print(output)


# Função auxiliar para criar uma lista Python grande (tamanho N)
def create_python_list(n):
    return list(range(n))


# Função auxiliar para criar a Lista Ligada grande (tamanho N)


def create_linked_list(n):
    ll = LinkedList()
    for i in range(n):
        # Usamos append, que é O(1) na nossa LL, para construir a lista de forma eficiente
        ll.append(i)
    return ll


"""
Cenário 1: Lista Ligada (Esperado: $O(1)$)
"""
TAMANHO = 10000

print(f"\n--- Teste 1: Inserção no Início (N={TAMANHO}) ---")

# Lista Ligada
ll = create_linked_list(TAMANHO)
start_time_ll = time.time()

# Inserindo TAMANHO novos elementos no início (prepend é O(1))
for i in range(TAMANHO):
    ll.prepend(i)

end_time_ll = time.time()
print(f"Lista Ligada (O(1)): {end_time_ll - start_time_ll:.6f} segundos")


"""
Cenário 2: Lista Python (Esperado: $O(n)$)
"""
# Lista Python
py_list = create_python_list(TAMANHO)
start_time_py = time.time()

# Inserindo TAMANHO novos elementos no início (insert(0, ...) é O(N))
for i in range(TAMANHO):
    py_list.insert(0, i)

end_time_py = time.time()
print(f"Lista Python (O(n)): {end_time_py - start_time_py:.6f} segundos")

"""
3. Teste de Performance 2: Acesso Aleatório (lookup)
"""

# Cenário 1: Lista Python (Esperado: $O(1)$)

TAMANHO_LOOKUP = 100000  # Usamos um tamanho maior para maior precisão

print(f"\n--- Teste 2: Acesso Aleatório (N={TAMANHO_LOOKUP}) ---")

# Lista Python (O(1))
py_list_lookup = create_python_list(TAMANHO_LOOKUP)
start_time_py = time.time()

# Acessa 10.000 elementos aleatórios
for _ in range(10000):
    index = random.randint(0, TAMANHO_LOOKUP - 1)
    _ = py_list_lookup[index]  # Acesso direto

end_time_py = time.time()
print(f"Lista Python (O(1)): {end_time_py - start_time_py:.6f} segundos")

# Cenário 2: Lista Ligada (Esperado: $O(n)$)
# Lista Ligada (O(n))
ll_lookup = create_linked_list(TAMANHO_LOOKUP)

# Precisamos de uma função helper para acessar por índice (lookup) na nossa LL


def ll_lookup_helper(ll, index):
    current = ll.head
    for _ in range(index):
        if current is None:
            return None
        current = current.next
    return current.data


start_time_ll = time.time()

# Acessa 10.000 elementos aleatórios usando a travessia O(n)
for _ in range(10000):
    index = random.randint(0, TAMANHO_LOOKUP - 1)
    ll_lookup_helper(ll_lookup, index)  # Travessia O(n)

end_time_ll = time.time()
print(f"Lista Ligada (O(n)): {end_time_ll - start_time_ll:.6f} segundos")
