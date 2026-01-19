class Node:
    """
    Representa um nó individual na árvore.
    """

    def __init__(self, value):
        self.value = value  # O dado que o nó armazena
        self.left = None   # Ponteiro para o filho menor (à esquerda)
        self.right = None  # Ponteiro para o filho maior (à direita)


class BinarySearchTree:
    """
    Gerenciador da árvore, responsável por organizar os nós.
    """

    def __init__(self):
        # A árvore começa vazia, sem raiz.
        self.root = None

    def insert(self, value):
        """
        Insere um novo valor respeitando a regra:
        Esquerda < Pai < Direita.
        Complexidade Média: O(log n)
        """
        new_node = Node(value)

        # Se a árvore está vazia, o novo nó torna-se a raiz.
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
            # BSTs básicas geralmente não aceitam valores duplicados.
            if value == temp.value:
                return False

            # Lógica para o lado ESQUERDO (Valores menores)
            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                # Move o cursor para o próximo nó à esquerda
                temp = temp.left

            # Lógica para o lado DIREITO (Valores maiores)
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                # Move o cursor para o próximo nó à direita
                temp = temp.right

    def contains(self, value):
        """
        Busca por um valor na árvore.
        Complexidade Média: O(log n)
        """
        temp = self.root

        # Percorre a árvore enquanto não chegar em um espaço vazio.
        while temp is not None:
            if value < temp.value:
                temp = temp.left   # Busca nos menores
            elif value > temp.value:
                temp = temp.right  # Busca nos maiores
            else:
                return True        # Valor encontrado!

        return False  # Percorreu o caminho e não encontrou.


# 1. Instancie sua árvore
minha_arvore = BinarySearchTree()

# 2. Insira alguns valores
minha_arvore.insert(47)
minha_arvore.insert(21)
minha_arvore.insert(76)
minha_arvore.insert(18)
minha_arvore.insert(27)

print(f"Árvore: {minha_arvore}")

# 3. Teste a busca
print(f"Existe 27? {minha_arvore.contains(27)}")  # Deve retornar True
print(f"Existe 10? {minha_arvore.contains(10)}")  # Deve retornar False
