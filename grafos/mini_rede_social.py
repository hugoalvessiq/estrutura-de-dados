# Representando uma mini rede social
grafo_social = {
    "Você": ["Alice", "Bob"],
    "Alice": ["Você", "Charlie"],
    "Bob": ["Você"],
    "Charlie": ["Alice"]
}

print(f"Amigos da Alice: {grafo_social['Alice']}")