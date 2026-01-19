class MiniHashTable:
    def __init__(self, size=7):
        # 1. 'data_map' é o array (lista Python) que armazena os buckets.
        # Inicializamos com 'None' em cada bucket.
        self.size = size
        self.data_map = [None] * size

    def __hash(self, key):
        """
        Gera o índice para a chave.
        Complexidade de Tempo: O(k), onde k é o tamanho da chave.
        """
        hash_value = 0

        # 1. Pega os valores numéricos (ASCII) de cada letra da chave.
        for letter in key:
            # Obtém o valor ASCII e adiciona ao acumulador.
            hash_value = (hash_value + ord(letter) * 1)

        # 2. Usa o operador MÓDULO (%) para garantir que o índice
        # esteja dentro do limite do tamanho do nosso array (0 a size-1).
        index = hash_value % self.size

        # 3. Retorna o índice (o bucket) onde a chave deve ser armazenada.
        return index

    def set(self, key, value):
        # 1. Gera o índice (bucket) para a chave
        index = self.__hash(key)

        # 2. Checa se o bucket está vazio (Colisão não ocorreu ainda)
        if self.data_map[index] is None:
            # Se vazio, inicializa o bucket com uma lista para armazenar os pares [chave, valor]
            self.data_map[index] = []

        # 3. Adiciona o par [chave, valor] ao bucket (lista)
        # Por causa do Separate Chaining, podemos ter múltiplos pares [c, v] aqui.
        self.data_map[index].append([key, value])

    def get(self, key):
        # 1. Gera o índice (bucket) para a chave. O(k)
        index = self.__hash(key)

        # 2. Obtém o bucket
        bucket = self.data_map[index]

        # 3. Se o bucket não estiver vazio:
        if bucket is not None:
            # 4. Percorre a lista dentro do bucket (Travessia O(l), onde l é o tamanho da lista de colisão)
            for pair in bucket:
                # pair é [chave, valor]
                if pair[0] == key:
                    # Chave encontrada! Retorna o valor. O(1)
                    return pair[1]

        # 5. Se o bucket estava vazio ou a chave não foi encontrada:
        return None


# Exemplo de teste (ainda sem o get):
ht = MiniHashTable()
ht.set('uva', 100)   # Assume index 3
ht.set('kiwi', 200)  # Assume index 3 (Colisão!)
ht.set('banana', 300)
print(ht.data_map)
# Saída esperada (se os hashes colidirem): [None, ..., [[uva, 100], [kiwi, 200]], ...]

print(ht.get("uva"))     # 100
print(ht.get("kiwi"))    # 200
print(ht.get("banana"))  # 300
print(ht.get("manga"))  # None

"""
COLISÕES
"""

ht = MiniHashTable(size=3)

ht.set("uva", 100)
ht.set("kiwi", 200)
ht.set("pera", 300)

print(ht.data_map)
print(ht.get("kiwi"))
