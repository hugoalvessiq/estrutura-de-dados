
class Node():
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
        if index < 0 or index > self.lenght:
            print('Erro: Índice fora dos limites')
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

        # O leader deve agora apontar paraa o novo nó
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


# Teste:

# 1. Cria uma nova lista
minha_lista = LinkedList()

# 2. Adiciona elementos no final (append)
minha_lista.append(10)  # Lista: 10 -> None
minha_lista.append(20)  # Lista: 10 -> 20 -> None

# 3. Adiciona elementos no início (prepend)
minha_lista.prepend(5)  # Lista: 5 -> 10 -> 20 -> None
minha_lista.prepend(1)  # Lista: 1 -> 5 -> 10 -> 20 -> None

# 4. Imprime o resultado
minha_lista.printList()  # Saída esperada: 1 -> 5 -> 10 -> 20 -> None

# 5. Imprime o tamanho
print(f"Tamanho da Lista: {minha_lista.length}")  # Saída esperada: 4
print(f"Head: {minha_lista.head.data}, \nTail: {
      minha_lista.tail.data}")  # Head: 1, Tail: 20
