class Node:
    """docstring for No"""

    def __init__(self, valor):
        self.valor = valor  # O conteúdo da vaga

        # O "bilhete" que aponta para o próximo (começa vazio)
        self.proximo = None


class ListLigada:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def adicionar(self, valor):
        novo_no = Node(valor)  # 1. Cria a pecinha

        if self.inicio is None:  # 2. A lista está vazia?
            self.inicio = novo_no
            self.fim = novo_no

        else:
            # Se já tem gente, o atual FIM aponta para o novo
            self.fim.proximo = novo_no
            # 4. E o novo nó agora é o novo FIM oficial
            self.fim = novo_no

    def imprimir_lista(self):
        atual = self.inicio  # Começa pelo primeiro
        while atual is not None:  # Enquanto não chegar no vazio...
            print(atual.valor, end=" -> ")
            # Qual linha de código faz o 'atual' pular para o próximo nó?
            atual = atual.proximo
        print("None")

    def buscar_valor(self, alvo):
        atual = self.inicio

        # 1. Primeiro garantimos que não estamos no vazio (None)
        while atual is not None:
            # 2. Comparamos o VALOR que está dentro do nó atual
            if atual.valor == alvo:
                print("Encontrou! 🎉")
                return True  # Encontrou! 🎉
            # Move o dedo pra o próximo nó
            atual = atual.proximo
        return False  # se sai do loop, é porque percorreu tudo e não achou

    def remover_valor(self, alvo):
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.valor == alvo:
                if anterior is None:  # Caso especial: remover o primeiro da lista
                    self.inicio = atual.proximo
                    if self.inicio is None:  # Se a lista ficou vazia
                        self.fim = None
                else:
                    # O "pulo do gato": o anterior pula o atual e liga no próximo
                    anterior.proximo = atual.proximo
                    if atual.proximo is None:  # Se removemos o último, atualizamos o fim
                        self.fim = anterior

                print(f"Valor {alvo} removido!")
                return True

            anterior = atual
            atual = atual.proximo
        return False


# --- TESTES PRÁTICOS ---
minha_lista = ListLigada()
minha_lista.adicionar(10)
minha_lista.adicionar(20)
minha_lista.adicionar(30)

print("Lista Original:")
minha_lista.imprimir_lista()

minha_lista.remover_valor(20)
print("Após remover 20:")
minha_lista.imprimir_lista()
