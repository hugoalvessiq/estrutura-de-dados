# Arquivo de testes para os algoritmos

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class LinkedList:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self, valor):
        novo_no = Node(valor)
        if not self.inicio:
            self.inicio = self.fim = novo_no
        else:
            self.fim.proximo = novo_no
            self.fim = novo_no

    def inverter(self):
        atual = self.inicio
        anterior = None
        while atual:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo
        self.fim = self.inicio
        self.inicio = anterior

    def para_lista(self):
        res = []
        atual = self.inicio
        while atual:
            res.append(atual.valor)
            atual = atual.proximo
        return res


def validar_parenteses(texto):
    pilha = []
    mapeamento = {')': '(', ']': '[', '}': '{'}

    for char in texto:
        if char in mapeamento.values():
            pilha.append(char)
        elif char in mapeamento:
            if not pilha or pilha[-1] != mapeamento[char]:
                return False
            pilha.pop()
    return len(pilha) == 0


# --- Execução de Testes ---
if __name__ == "__main__":
    # Teste 1: Inverter Lista
    ll = LinkedList()
    for i in [1, 2, 3]:
        ll.adicionar(i)
    print(f"Original: {ll.para_lista()}")
    ll.inverter()
    print(f"Invertida: {ll.para_lista()}")

    # Teste 2: Validar Parênteses
    testes = ["([])", "([)]", "{[]()}"]
    for t in testes:
        print(f"Texto '{t}' é válido? {validar_parenteses(t)}")
