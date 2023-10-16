def quick_sort(lista):
    quick_sort_aux(lista, 0, len(lista) - 1)

def quick_sort_aux(lista, inicio, fim):
    if inicio < fim:
        p = particao(lista, inicio, fim)
        quick_sort_aux(lista, inicio, p - 1)
        quick_sort_aux(lista, p + 1, fim)

def particao(lista, inicio, fim):
    i = inicio - 1
    pivo = lista[fim]
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1

# Teste do resultado:

lista = [4, 7, 3, 2, 6, 1, 8, 9, 5]
print("Lista Original: {}".format(lista))
quick_sort(lista)
print("Lista Ordenada: {}".format(lista))
