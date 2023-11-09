def busca_sequencial(A, chave, N):
    for i in range (0,N):
        if (A[i][0] == chave):
            return A[i][1];
    return "Aluno não encontrado"

A= [["Matheus", "Ciência da Computação"], ["Arthur", "Administração"], ["Juliana", "Engenharia Eletrica"], ["Carolina", "Letras"], ["Luana", "Relções Publicas"]]

chave = input("Digite o nome de um aluno para pesquisa:")
N = len(A);

resultado = busca_sequencial(A, chave, N)
print(resultado)