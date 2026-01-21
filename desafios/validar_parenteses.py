def validar_parenteses(texto):
    pilha = []  # Pilha que guardará os símbolos de abertura
    # Dica: use um dicionário para mapear quem fecha quem
    mapeamento = {')': '(', ']': '[', '}': '{'}
    # Aberturas # {'(', '[', '{'}
    aberturas = mapeamento.values()

    for caractere in texto:
        # Se for um símbolo de abertura, empilha
        if caractere in aberturas:
            pilha.append(caractere)

        # Se for um símbolo de fechamento, verifica correspondência
        elif caractere in mapeamento:
            # Se a pilha está vazia ou o topo não corresponde ao esperado,
            # o texto está desbalanceado.
            if not pilha or pilha[-1] != mapeamento[caractere]:
                return False

            # Caso corresponda, remove o símbolo de abertura da pilha
            pilha.pop()
    return len(pilha) == 0


validar_parenteses('([{')
# validar_parenteses('[')
# validar_parenteses('{')
validar_parenteses(')]}')
