class MinhaHashTable:
    def __init__(self, tamanho=10):
        # Criamos 'buckets' (baldes). Cada balde é uma lista para tratar colisões.
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _funcao_hash(self, chave):
        # Transforma o texto em um número e usa o resto da divisão pelo tamanho
        # Isso garante que o índice sempre caiba na nossa lista
        return hash(chave) % self.tamanho

    def guardar(self, chave, valor):
        indice = self._funcao_hash(chave)
        # Guardamos como um par [chave, valor] dentro do balde
        self.tabela[indice].append([chave, valor])
        print(f"'{chave}' guardado no índice {indice}")

    def buscar(self, chave):
        indice = self._funcao_hash(chave)
        # Procuramos dentro do balde específico (caso haja colisão)
        for par in self.tabela[indice]:
            if par[0] == chave:
                return par[1]
        return None


# --- Testando ---
meu_mapa = MinhaHashTable()
meu_mapa.guardar("João", "9999-1111")
meu_mapa.guardar("Maria", "8888-2222")

print(f"Tel da Maria: {meu_mapa.buscar('Maria')}")
