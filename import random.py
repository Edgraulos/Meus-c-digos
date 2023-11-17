import random

def partition(seq, low, high):
    """
    Função que realiza o particionamento do Quicksort.
    Argumentos:
    seq: A lista a ser ordenada.
    low: O índice de início da sublista.
    high: O índice de fim da sublista.
    Retorna:
    O índice do pivot após o particionamento.
    """
    pivot_index = random.randint(low, high - 1)  # Escolhe um índice aleatório como pivot
    pivot = seq[pivot_index]  # Valor do pivot
    seq[pivot_index], seq[high - 1] = seq[high - 1], seq[pivot_index]  # Move o pivot para o final
    i = low  # Índice do elemento menor encontrado
    for j in range(low, high - 1):
        if seq[j] < pivot:
            seq[i], seq[j] = seq[j], seq[i]  # Troca elementos menores para a esquerda do pivot
            i += 1
    seq[i], seq[high - 1] = seq[high - 1], seq[i]  # Coloca o pivot em sua posição correta
    return i

def quicksort(seq):
    """
    Função principal do Quicksort.
    """
    def quicksort_helper(seq, low, high):
        """
        Função auxiliar recursiva para ordenar a sublista.
        """
        if low < high - 1:
            pivot_index = partition(seq, low, high)  # Realiza o particionamento
            quicksort_helper(seq, low, pivot_index)  # Ordena a sublista à esquerda do pivot
            quicksort_helper(seq, pivot_index + 1, high)  # Ordena a sublista à direita do pivot

    quicksort_helper(seq, 0, len(seq))  # Chama a função auxiliar para ordenar toda a lista

# Exemplo de uso
numbers = [5, 8, 2, 6, 9, 1, 0, 7]
quicksort(numbers)  # Chama a função para ordenar a lista
print(numbers)
