from collections import deque


class SistemaAtendimento:
    def __init__(self):
        # O deque é ideal para filas FIFO (First-In, First-Out)
        self.fila = deque()

    def chegar_cliente(self, nome: str):
        """Equivalente ao Enqueue: O(1)"""
        print(f"🔔 Cliente {nome} entrou na fila.")
        self.fila.append(nome)

    def atender_cliente(self):
        """Equivalente ao Dequeue: O(1)"""
        if not self.fila:
            print("⚠️ A fila está vazia! Nenhum cliente para atender.")
            return None

        # Remove do INÍCIO da fila
        cliente_atendido = self.fila.popleft()
        print(f"✅ Atendendo agora: {cliente_atendido}")
        return cliente_atendido

    def ver_fila(self):
        """Visualiza quem está esperando: O(n)"""
        if not self.fila:
            print("📭 Fila vazia.")
        else:
            print(f"\n📋 Fila atual: {' -> '.join(self.fila)}")


# --- Teste do Sistema ---
banco = SistemaAtendimento()

banco.chegar_cliente("Alice")
banco.chegar_cliente("Bruno")
banco.chegar_cliente("Carla")

banco.ver_fila()

banco.atender_cliente()
banco.ver_fila()

banco.atender_cliente()
banco.atender_cliente()
banco.atender_cliente()  # Tentativa com fila vazia
