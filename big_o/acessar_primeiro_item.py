def acessar_primeiro_item(lista):
    for indice, item in enumerate(lista):
        if indice == 0:
            print(f"A fruta na posição {indice} é {item}")
            break


def acessar_primeiro_item_otimizado(lista):
    # Acesso direto pelo índice (Lookup)
    if lista:  # Verifica se a lista não está vazia
        print(f"O item na posição 0 é {lista[0]}")


# acessar_primeiro_item(["maçã", "banana", "cereja", "melão", "laranja"])
acessar_primeiro_item_otimizado(
    ["maçã", "banana", "cereja", "melão", "laranja"])
