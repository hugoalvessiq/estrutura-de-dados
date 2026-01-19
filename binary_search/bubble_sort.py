def bubble_sort(lista):
    n = len(lista)
    # O loop externo controla quantas vezes passamos pela lista
    for i in range(n):
        # O loop interno compara os vizinhos
        # Note que a cada volta, o final da lista já está ordenado (n-i-1)
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Se o da esquerda for maior, eles trocam! 🔄
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
