def encontrar_maior_numero(lista: list) -> int:
    # 1. Checagem de segurança: Se a lista estiver vazia, retornamos algo (ex: 0 ou erro).
    if not lista:
        return 0  # Ou levante um erro, dependendo da especificação

    # 2. Inicialização:
    # Definimos o maior número *inicial* como o primeiro elemento da lista.
    # Isso resolve o problema de listas com números negativos.
    maior_numero_atual = lista[0]

    # 3. Iteração e Comparação:
    # Percorremos a lista a partir do SEGUNDO elemento (índice 1),
    # pois o primeiro já foi usado para inicialização.
    for i in range(1, len(lista)):
        elemento_atual = lista[i]

        # Comparamos o elemento atual com o maior que encontramos até agora.
        if elemento_atual > maior_numero_atual:
            # 4. Atualização:
            # Se for maior, ele se torna o novo 'maior_numero_atual'.
            maior_numero_atual = elemento_atual

    # 5. Retorno: O resultado final.
    return maior_numero_atual


# Exemplo de uso para teste
print(f"Lista [3, 1, 4, 1, 5, 9, 2, 6]: {
      encontrar_maior_numero([3, 1, 4, 1, 5, 9, 2, 6])}")
print(f"Lista [-5, -1, -8, -2]: {encontrar_maior_numero([-5, -1, -8, -2])}")
