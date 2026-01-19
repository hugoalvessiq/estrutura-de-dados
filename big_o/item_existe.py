def item_existe(lista: list, item_buscado: any) -> bool:  # type: ignore
    # 1. Iteração: Percorremos CADA elemento da lista.
    for elemento in lista:

        # 2. Comparação e Saída Otimizada (Melhor Caso):
        if elemento == item_buscado:
            # Se encontrarmos, RETORNAMOS TRUE IMEDIATAMENTE.
            # O algoritmo termina aqui, sem precisar ver o resto da lista.
            return True

    # 3. Pior Caso:
    # Se o loop terminar sem encontrar o item, significa que ele não existe na lista.
    # O loop rodou N vezes (seja o item o último ou se não existir).
    return False


# Exemplo de uso
minha_lista = [10, 20, 30, 40, 50]
print(f"O item 20 existe? {item_existe(minha_lista, 20)}")
print(f"O item 100 existe? {item_existe(minha_lista, 100)}")
