def insertion_sort(lista):
    # Começamos do segundo elemento (índice 1)
    for i in range(1, len(lista)):
        valor_atual = lista[i]
        j = i - 1

        # Enquanto o vizinho da esquerda for maior que o nosso valor_atual
        while j >= 0 and valor_atual < lista[j]:
            # Empurramos o vizinho para a direita
            lista[j + 1] = lista[j]
            j -= 1

        # Encaixamos o valor_atual no espaço que sobrou
        lista[j + 1] = valor_atual

    return lista
