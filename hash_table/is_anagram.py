def is_anagram(str1: str, str2: str) -> bool:
    """
    Verifica se duas strings são anagramas usando uma Hash Table (Dicionário).
    Complexidade de Tempo: O(n) (linear)
    """
    # 1. Pré-checagem de O(1): Se os tamanhos são diferentes, não pode ser anagrama.
    # Se você quiser ignorar espaços, precisaria remover ou contar apenas letras.
    if len(str1) != len(str2):
        return False

    # A Hash Table (dicionário) que armazena a contagem de letras da str1.
    char_counts = {}

    # --- FASE 1: Contagem de str1 (O(n)) ---
    for char in str1.lower():
        # Corrige o erro de sintaxe: chama .get() no dicionário (char_counts).
        # Se a chave existe, incrementa. Se não, o valor default (0) é usado e incrementado para 1.
        char_counts[char] = char_counts.get(char, 0) + 1

    # --- FASE 2: Verificação de str2 (O(n)) ---
    # Este loop está separado do anterior!
    for char in str2.lower():

        # O(1) Lookup: Verifica se a letra existe e se ainda há contagem positiva.
        if char not in char_counts or char_counts[char] == 0:
            # Se a letra não está em str1 ou se já usamos todas as ocorrências: FALHA!
            return False

        # Diminui a contagem, pois encontramos uma correspondência.
        char_counts[char] -= 1

    # --- FASE 3: Verificação Final (Desnecessária, mas pode ser incluída) ---
    # Como checamos no início se os comprimentos são iguais, a FASE 2 garante que,
    # se chegarmos até aqui, todas as contagens serão zero.

    return True


# --- Exemplos de Teste ---
print(f"'amor' e 'roma': {is_anagram('amor', 'roma')}")            # True
print(f"'alegria' e 'regalia': {is_anagram('alegria', 'regalia')}")  # True
# False (tamanho igual, mas 2 's' e 1 't' no 2º)
print(f"'teste' e 'setse': {is_anagram('teste', 'setse')}")
# False (tamanhos diferentes)
print(f"'teste' e 'tste': {is_anagram('teste', 'tste')}")
print(f"'listen' e 'silent': {is_anagram('listen', 'silent')}")    # True
