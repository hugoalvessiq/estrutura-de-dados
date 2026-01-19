def selection_sort(lista):
    n = len(lista)
    # Percorremos a lista para definir cada posição i
    for i in range(n):
        indice_minimo = i
        # Procuramos o menor valor no
        # restante da lista (da posição i+1 em diante)
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j

        # Trocamos o valor da posição atual pelo menor encontrado
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]

    return lista
