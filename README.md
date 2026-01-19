# 📚 **Plano de Estudos de Estruturas de Dados**

*Do básico ao avançado, com teoria + prática.*

---

## 🗓️ **Fundamentos de Estruturas de Dados**

### 🎯 **Objetivo**

Construir a base: entender o que são estruturas de dados, big-O e como pensar algoritmicamente.

---

### 📘 **Teoria**

- O que são estruturas de dados?
- Diferença entre estrutura **linear** e **não linear**
- Memória RAM, stack vs heap (visão simplificada)
- O que é **complexidade de tempo e espaço**
- Notação Big-O:

  - O(1), O(n), O(n²), O(log n), O(n log n)

- Diferença entre **Array** e **List** em Python
- Tipos primitivos e compostos

---

### 🛠️ **Prática**

**Projeto 1: Analisador de Complexidade Simples**

- Crie funções como:

  - encontrar o maior número em uma lista
  - verificar se um item existe
  - somar todos os elementos

- Depois, escreva você mesmo qual é a complexidade Big-O.

**Versões:**

- Python
- JavaScript

---

## 🗓️ **Arrays, Listas e Manipulação de Coleções**

### 🎯 **Objetivo**

Aprender manipulação eficiente de listas/arrays e entender como funcionam internamente.

---

### 📘 **Teoria**

- Arrays estáticos vs dinâmicos
- Listas ligadas (linked lists):

  - singly linked list
  - doubly linked list

- Operações:

  - push, pop, unshift, shift
  - insert
  - delete
  - lookup (acesso)
  - traversal (percorrer lista)

---

### 🛠️ **Prática**

**Projeto 2: Implementar sua própria Lista Ligada**

- Criar nó (Node)
- Criar classe LinkedList
- Métodos:

  - append
  - prepend
  - insertAt
  - removeAt
  - printList

**Bônus**: medir performance vs array normal.

---

## 🗓️ **Pilhas (Stacks) e Filas (Queues)**

### 🎯 **Objetivo**

Aprender estruturas lineares muito usadas em algoritmos e processos computacionais.

---

### 📘 **Teoria**

- Conceito LIFO e FIFO
- Implementação com lista/array
- Implementação com ponteiros (links)
- Aplicações reais:

  - desfazer/refazer
  - chamadas de função
  - sistemas de impressão
  - buffers

---

### 🛠️ **Prática**

**Projeto 3: Simulador de Desfazer/Refazer (Undo/Redo)**

- Use duas pilhas
- Interface simples no terminal

**Projeto 4: Sistema de filas de atendimento**

- Filas com prioridade opcional
- Entrada e saída

---

## 🗓️ **Hash Tables (Mapas e Dicionários)**

### 🎯 **Objetivo**

Entender hashing, colisões, distribuição e por que dicionários/objetos são tão rápidos.

---

### 📘 **Teoria**

- Hash function
- Colisões: chaining vs open addressing
- Operações: get, set, delete
- Complexidade real (> O(1) na maioria dos casos)
- Implementação interna em Python e JavaScript

---

### 🛠️ **Prática**

**Projeto 5: Criar sua própria Hash Table**

- buckets
- função hash simples
- métodos:

  - set
  - get
  - remove
  - keys
  - values

**Projeto 6 (curto):**
Criar um validador de anagramas usando hash table.

---

## 🗓️ **Árvores (Trees)**

### 🎯 **Objetivo**

Entender estruturas hierárquicas e treinar recursão.

---

### 📘 **Teoria**

- Árvores: raiz, nós, folhas, altura
- Árvores binárias
- Árvores binárias de busca (BST)
- Traversal:

  - in-order
  - pre-order
  - post-order
  - breadth-first search (BFS)
  - depth-first search (DFS)

---

### 🛠️ **Prática**

**Projeto 7: Implementar uma Binary Search Tree**

- insert
- find
- remove
- BFS
- DFS
- altura da árvore

**Projeto 8: Criar um menu de navegação hierárquico**

- Representado com árvore
- Mostrar submenus (recursão)

---

## 🗓️ **Heaps & Priority Queues**

### 🎯 **Objetivo**

Aprender estruturas usadas em algoritmos de performance e sistemas de prioridade.

---

### 📘 **Teoria**

- Heap (min-heap e max-heap)
- Priority Queue
- Representação em array
- Operações:

  - heapify
  - push
  - pop
  - peek

---

### 🛠️ **Prática**

**Projeto 9: Construir um Min-Heap e um Max-Heap**

- Armazenar em array
- Implementar:

  - insert
  - extract
  - heapify

**Projeto 10: Sistema de tarefas com prioridade**

- Adicionar tarefa com prioridade
- Extrair próxima tarefa

---

## 🗓️ **Grafos (Graphs)**

### 🎯 **Objetivo**

Dominar conceitos de grafos, muito usados em IA, redes, mapas e jogos.

---

### 📘 **Teoria**

- Representação:

  - lista de adjacência
  - matriz de adjacência

- Tipos:

  - direcionado / não direcionado
  - ponderado / não ponderado

- BFS em grafos
- DFS em grafos
- Detecção de ciclos
- Caminho mais curto:

  - Dijkstra (básico)
  - A\* (introdução leve)

---

### 🛠️ **Prática**

**Projeto 11: Grafo de Amigos (rede social simples)**

- adicionar amigo
- remover
- listar conexões
- verificar se dois usuários estão conectados via BFS

**Projeto 12: Caminho mais curto entre cidades**

- grafo ponderado
- algoritmo de Dijkstra

---

## 🗓️ **Estruturas Avançadas + Projeto Final**

### 🎯 **Objetivo**

Consolidar todo o conteúdo com estruturas avançadas e projeto robusto.

---

### 📘 **Teoria**

- Tries (árvores de prefixo)
- AVL Trees (introdução)
- Red-Black Trees (visão)
- Segment Trees (visão)
- Algoritmos clássicos:

  - merge sort
  - quick sort

---

### 🛠️ **Prática**

### **Projeto Final — Sistema Completo de Pesquisa e Indexação**

Você irá combinar várias estruturas:

Features:

- Indexação de palavras usando **Trie**
- Registro de documentos em **Hash Table**
- Fila de prioridade para buscas recentes
- Grafo de hiperlinks entre documentos
- Ranking simples baseado em conexões (PageRank simplificado)

Extras:

- Interface CLI estilizada
- Exportar resultados para JSON

---
