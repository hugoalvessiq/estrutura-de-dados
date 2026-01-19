class EditorTexto:
    def __init__(self):
        self.texto = ""
        self.historico = []  # Esta é a nossa Pilha (Stack)

    def escrever(self, novo_texto):
        # Antes de mudar, guardamos o estado atual na Pilha
        self.historico.append(self.texto)
        self.texto += novo_texto
        print(f"Texto atual: '{self.texto}'")

    def desfazer(self):
        if len(self.historico) > 0:
            # O último a entrar (LIFO) é o que sai para restaurar
            self.texto = self.historico.pop()
            print(f"Desfeito! Texto agora: '{self.texto}'")
        else:
            print("Nada para desfazer.")


# --- Testando a Pilha ---
meu_editor = EditorTexto()
meu_editor.escrever("Olá ")
meu_editor.escrever("Mundo")
meu_editor.escrever("!")

meu_editor.desfazer()  # Remove o "!"
meu_editor.desfazer()  # Remove o "Mundo"
meu_editor.desfazer()  # Remove o "Mundo"
meu_editor.desfazer()  # Remove o "Mundo"
