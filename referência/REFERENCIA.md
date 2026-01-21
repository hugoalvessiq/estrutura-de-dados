

# 📚 Material de Referência: Estruturas de Dados e Algoritmos (Semanas 1-8)

Este documento consolida os conceitos fundamentais e as implementações práticas desenvolvidas.

🏗️ **1. Fundamentos e Notação Big-O**

- **O(1)**: Tempo constante. Acesso direto (ex: índices de array, chaves de dicionário).
- **O(n)**: Tempo linear. Percorre todos os elementos (ex: busca em lista ligada).
- **O(\log n)**: Tempo logarítmico. Divide o problema ao meio (ex: busca binária).

🔗 **2. Lista Ligada (Linked List)**

Estrutura composta por Nós. Cada nó armazena um valor e um ponteiro próximo.

- **Vantagem**: Inserção e remoção rápidas nas extremidades.
- **Desvantagem**: Acesso lento a elementos no meio.
- **Desafio**: Inversão de Lista

```python
def inverter(self):
    atual = self.inicio
    anterior = None
    while atual is not None:
        proximo = atual.proximo  # Salva o futuro
        atual.proximo = anterior  # Inverte a seta
        anterior = atual          # Move o 'passado' para frente
        atual = proximo           # Move o 'presente' para frente
    
    self.fim = self.inicio
    self.inicio = anterior
```

🥞 **3. Pilha (Stack)**

Segue o princípio LIFO (Last In, First Out).

- **Uso**: Histórico de navegação, botão desfazer, validação de sintaxe.
- **Desafio**: Validar Parênteses

```python
def validar_parenteses(texto):
    pilha = []
    mapeamento = {')': '(', ']': '[', '}': '{'}
    aberturas = mapeamento.values()

    for caractere in texto:
        if caractere in aberturas:
            pilha.append(caractere)
        elif caractere in mapeamento:
            if not pilha or pilha[-1] != mapeamento[caractere]:
                return False
            pilha.pop()
    
    return len(pilha) == 0
```

🗺️ **4. Hash Table (Dicionários)**

Usa uma função hash para acesso **$O(1)$**.

- **Colisões**: Resolvidas com Encadeamento (listas ligadas nos índices) ou Endereçamento Aberto.

🌳 **5. Árvores e Heaps**

- **BST**: Organização hierárquica (Esquerda < Pai < Direita).
- **Heap**: Prioridade constante. O maior (ou menor) está sempre na raiz.

🕸️ **6. Grafos**

- Representam relacionamentos complexos.
- **BFS (Busca em Largura)**: Usa uma Fila para explorar vizinhos por nível.
- **Dijkstra**: Encontra o caminho mais curto somando os "pesos" das arestas.

**Dica**: Pratique visualizando os ponteiros como mãos que seguram endereços de memória.
