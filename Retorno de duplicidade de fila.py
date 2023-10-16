# Filas de senhas dos dois totens
não_preferencial = [1, 2, 3, 4, 5, 6, 7]
preferencial = [4, 5, 6, 7, 8, 9, 10]

# Converter as filas em conjuntos (sets) para facilitar a comparação
set_não_preferencial = set(não_preferencial)
set_preferencial = set(preferencial)

# Encontrar números em duplicidade
numeros_em_duplicidade = set_não_preferencial.intersection(set_preferencial)

# Converter o resultado de volta em uma lista, se necessário
numeros_em_duplicidade_lista = list(numeros_em_duplicidade)

# Exibir os números em duplicidade
print("Números em duplicidade nas filas:", numeros_em_duplicidade_lista)
