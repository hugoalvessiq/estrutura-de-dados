"""
  Exemplo Heap - Mini projeto Pronto Socorro
"""

import heapq


class ProntoSocorro:
    def __init__(self):
        self.fila_prioridade = []

    def adicionar_paciente(self, nome, urgencia):
        # O heapq usa o primeiro item da tupla para ordenar.
        # Nível 1 = Urgente, Nível 5 = Leve.
        heapq.heappush(self.fila_prioridade, (urgencia, nome))
        print(f"Paciente {nome} (Urgência {urgencia}) adicionado.")

    def atender_proximo(self):
        if self.fila_prioridade:
            urgencia, nome = heapq.heappop(self.fila_prioridade)
            print(f"ATENDENDO AGORA: {nome} (Nível de urgência: {urgencia})")
        else:
            print("Ninguém na fila.")


# --- Testando o Heap ---
hospital = ProntoSocorro()
hospital.adicionar_paciente("João (Gripe)", 5)
hospital.adicionar_paciente("Maria (Fratura)", 2)
hospital.adicionar_paciente("José (Infarto)", 1)

print("\n--- Iniciando Atendimento ---")
hospital.atender_proximo()  # Sai José (1) primeiro, mesmo sendo o último a chegar!
hospital.atender_proximo()  # Depois Maria (2)
