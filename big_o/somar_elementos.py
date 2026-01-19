def somar_elementos(lista: list) -> int:
    somar_total = 0

    for elemento in lista:
        somar_total += elemento

    return somar_total


print(f"Soma de [1, 2, 3, 4, 5]: {somar_elementos([1, 2, 3, 4, 5])}")
