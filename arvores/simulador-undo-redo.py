class UndoRedoSimulator:
    """
    Simula o sistema Desfazer/Refazer usando duas pilhas (LIFO).
    As listas Python são usadas como pilhas, pois append/pop são O(1).
    """

    def __init__(self):
        # Pilha de Ações (Guarda o histórico de ações feitas)
        self.undo_stack = []
        # Pilha de Refazer (Guarda as ações que foram desfeitas)
        self.redo_stack = []

    def do_action(self, action: str):
        """Executa uma nova ação. Push na pilha de undo."""
        print(f"-> AÇÃO REALIZADA: '{action}'")

        # 1. Coloca a nova ação no topo da pilha de Desfazer.
        self.undo_stack.append(action)  # O(1)

        # 2. Quando uma nova ação é feita, a pilha de Refazer é zerada.
        # Não podemos refazer algo se fizemos algo novo!
        self.redo_stack = []

    def undo(self):
        """Desfaz a última ação. Pop do undo, Push no redo."""

        # Checagem de segurança: Só podemos desfazer se houver ações no histórico.
        if not self.undo_stack:
            print("\n❌ Nenhuma ação para desfazer.")
            return None

        # 1. Remove a última ação da pilha de Desfazer (Pop).
        action_to_undo = self.undo_stack.pop()  # O(1)

        # 2. Move essa ação para o topo da pilha de Refazer (Push).
        self.redo_stack.append(action_to_undo)  # O(1)

        print(f"\n<- DESFEITO: '{action_to_undo}'")
        return action_to_undo

    def redo(self):
        """Refaz a última ação desfeita. Pop do redo, Push no undo."""

        # Checagem de segurança: Só podemos refazer se houver ações desfeitas.
        if not self.redo_stack:
            print("\n❌ Nenhuma ação para refazer.")
            return None

        # 1. Remove a última ação da pilha de Refazer (Pop).
        action_to_redo = self.redo_stack.pop()  # O(1)

        # 2. Move essa ação de volta para a pilha de Desfazer (Push).
        self.undo_stack.append(action_to_redo)  # O(1)

        print(f"-> REFEITO: '{action_to_redo}'")
        return action_to_redo


editor = UndoRedoSimulator()

print("--- Cenário 1: Fazendo Ações ---")
editor.do_action("Escrever 'Olá'")
editor.do_action("Adicionar figura")
editor.do_action("Mudar cor do fundo")

print("\n--- Cenário 2: Desfazendo (LIFO) ---")
# Desfaz a última (Mudar cor do fundo)
editor.undo()
# Desfaz a penúltima (Adicionar figura)
editor.undo()

print("\n--- Cenário 3: Refazendo ---")
# Refaz a última desfeita (Adicionar figura)
editor.redo()
# Refaz a penúltima desfeita (Mudar cor do fundo)
editor.redo()

print("\n--- Cenário 4: Refazer/Novo Conflito ---")
# Desfaz uma vez (Mudar cor do fundo)
editor.undo()
print(f"\nEstado da Pilha UNDO: {editor.undo_stack}")
print(f"Estado da Pilha REDO: {editor.redo_stack}")

# Faz uma NOVA AÇÃO: Zera a pilha REDO!
editor.do_action("Salvar arquivo")

print(f"\nEstado da Pilha UNDO após nova ação: {editor.undo_stack}")
print(f"Estado da Pilha REDO após nova ação: {
      editor.redo_stack}")  # Deve estar vazia
editor.redo()  # Deve mostrar a mensagem de erro "Nenhuma ação para refazer."
