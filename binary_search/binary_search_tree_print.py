class Node:
    """Representa um nó individual na árvore."""

    def __init__(self, value):
        self.value = value          # O dado que o nó armazena
        self.left = None           # Filho menor (esquerda)
        self.right = None          # Filho maior (direita)

    def __repr__(self):
        # Representação curta que ajuda na depuração
        return f"Node({self.value})"


class BinarySearchTree:
    """Gerenciador da árvore, responsável por organizar os nós."""

    def __init__(self):
        self.root = None

    # ------------------------------------------------------------
    # Inserção
    # ------------------------------------------------------------
    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
            if value == temp.value:
                return False          # não aceita duplicatas

            if value < temp.value:    # vai para a esquerda
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:                     # vai para a direita
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    # ------------------------------------------------------------
    # Busca
    # ------------------------------------------------------------
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    # ------------------------------------------------------------
    # Métodos de representação
    # ------------------------------------------------------------
    def _traverse_in_order(self, node, acc):
        """Percorre a sub‑árvore em ordem crescente e acumula os valores."""
        if node is None:
            return
        self._traverse_in_order(node.left, acc)
        acc.append(str(node.value))
        self._traverse_in_order(node.right, acc)

    def __str__(self):
        """Retorna uma string legível – lista de valores em ordem crescente."""
        if self.root is None:
            return "Árvore vazia"
        values = []
        self._traverse_in_order(self.root, values)
        return " -> ".join(values)

    # ------------------------------------------------------------
    # Visualização “árvore” opcional
    # ------------------------------------------------------------
    def _pretty(self, node, prefix="", is_left=True):
        """Constrói uma visualização tipo árvore usando recursão."""
        if node is None:
            return ""
        result = ""
        # Primeiro processamos o filho direito (para ficar acima)
        if node.right:
            result += self._pretty(
                node.right,
                prefix + ("│   " if is_left else "    "),
                False,
            )
        # Linha do nó atual
        result += prefix + ("├── " if is_left else "└── ") + \
            str(node.value) + "\n"
        # Depois o filho esquerdo (fica abaixo)
        if node.left:
            result += self._pretty(
                node.left,
                prefix + ("    " if is_left else "│   "),
                True,
            )
        return result

    def pretty_print(self):
        """Imprime a árvore inteira com estrutura hierárquica."""
        if self.root is None:
            print("Árvore vazia")
        else:
            # A raiz não tem prefixo nem “lado”
            print(str(self.root.value))
            if self.root.right:
                print(self._pretty(self.root.right, "", False), end="")
            if self.root.left:
                print(self._pretty(self.root.left, "", True), end="")


# ------------------- Uso -------------------
minha_arvore = BinarySearchTree()
for v in [47, 21, 76, 18, 27]:
    minha_arvore.insert(v)

# Impressão simples (valores em ordem crescente)
print(f"Árvore (in‑order): {minha_arvore}")

# Impressão “bonita” com estrutura de árvore
print("\nVisualização hierárquica:")
minha_arvore.pretty_print()

# Teste de busca
print(f"\nExiste 27? {minha_arvore.contains(27)}")   # True
print(f"Existe 10? {minha_arvore.contains(10)}")   # False
