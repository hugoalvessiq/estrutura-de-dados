# Nós
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    # Inserção usando RECURSÃO
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(valor, self.raiz)

    def _inserir_recursivo(self, valor, no_atual):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(valor, no_atual.esquerda)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._inserir_recursivo(valor, no_atual.direita)

    # Percurso Em-Ordem
    def em_ordem(self, no_atual):
        if no_atual:
            self.em_ordem(no_atual.esquerda)  # Vai tudo para a esquerda
            print(no_atual.valor, end=" ")    # Visita a raiz
            self.em_ordem(no_atual.direita)  # Vai tudo para a direita


# --- Executando o Projeto ---
minha_arvore = ArvoreBinaria()
elementos = [50, 30, 70, 20, 40, 60, 80]

for e in elementos:
    minha_arvore.inserir(e)

print("Caminho Em-Ordem (Ordenado):")
minha_arvore.em_ordem(minha_arvore.raiz)
