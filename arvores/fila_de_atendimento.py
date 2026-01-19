from collections import deque

class QueueSimulator:
    def __init__(self):
        # Usamos deque, onde append/pop nas duas extremidades são O(1)
        self.items = deque()

    def enqueue(self, item):
        """Adicionar ao final da fila (Push)."""
        self.items.append(item)

    def dequeue(self):
        """Remover do início da fila (Pop)."""
        if not self.items:
            print("\n❌ Fila vazia.")
            return None
        return self.items.popleft()
