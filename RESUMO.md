### 1. Material de Referência: Fundamentos de Estruturas de Dados 📚

Este resumo cobre os pontos principais.

| Estrutura / Conceito | Lógica Principal | Complexidade (Médio) | Uso Comum |
| --- | --- | --- | --- |
| **Array (Lista)** | Espaço contíguo na memória. Acesso direto via índice. | Acesso:  / Busca:  | Armazenar coleções simples. |
| **Busca Binária** | Divide o conjunto ordenado ao meio a cada passo. | Busca:  | Encontrar itens em listas grandes e ordenadas. |
| **Lista Ligada** | Nós espalhados conectados por ponteiros (`proximo`). | Inserção:  / Busca:  | Listas que mudam de tamanho frequentemente. |
| **Pilha (Stack)** | **LIFO**: Último a entrar, primeiro a sair. | Push/Pop:  | Desfazer (Undo), chamadas de função. |
| **Fila (Queue)** | **FIFO**: Primeiro a entrar, primeiro a sair. | Enq/Deq:  | Filas de impressão, processamento de tarefas. |
| **Hash Table** | Converte chave em índice via Função Hash. | Busca/Inserção:  | Dicionários, bancos de dados, caches. |
| **Árvore (BST)** | Hierárquica. Esquerda < Pai < Direita. | Busca:  | Organização de pastas, sistemas de busca. |
| **Grafo** | Conexões livres (Nós e Arestas). | Depende do algoritmo | Redes sociais, GPS (caminhos curtos). |

**Regra de Ouro da Memória 🧠:**

* **Ponteiros (`self.proximo`)**: São o "endereço" de onde o próximo dado está.
* **Recursão**: Uma função que chama a si mesma até atingir um "Caso Base" (parada).

