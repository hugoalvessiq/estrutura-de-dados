# ---------- implementação da lista ligada ----------
class No:
    """Um nó da lista ligada contendo um valor e referência ao próximo nó."""

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class ListaLigada:
    def __init__(self):
        self.inicio = None   # primeiro nó da lista
        self.fim = None      # último nó da lista

    # método auxiliar para acrescentar ao final (para montar o teste)
    def anexar(self, valor):
        novo_no = No(valor)
        if self.inicio is None:          # lista vazia
            self.inicio = self.fim = novo_no
        else:
            self.fim.proximo = novo_no   # liga ao último nó existente
            self.fim = novo_no           # atualiza referência ao novo fim

    # método que queremos testar
    def inverter(self):
        atual = self.inicio
        anterior = None

        while atual is not None:
            proximo = atual.proximo
            atual.proximo = anterior
            anterior = atual
            atual = proximo

        # troca as referências externas
        self.fim = self.inicio
        self.inicio = anterior

    # utilidade para imprimir a lista de forma legível
    def __str__(self):
        valores = []
        p = self.inicio
        while p is not None:
            valores.append(str(p.valor))
            p = p.proximo
        return " -> ".join(valores) + " -> None"


# ---------- teste ----------
if __name__ == "__main__":
    # cria a lista A -> B -> C -> None
    lista = ListaLigada()
    lista.anexar('A')
    lista.anexar('B')
    lista.anexar('C')

    print("Antes de inverter:")
    print(lista)          # saída esperada: A -> B -> C -> None

    # inverte a lista
    lista.inverter()

    print("\nDepois de inverter:")
    print(lista)          # saída esperada: C -> B -> A -> None
