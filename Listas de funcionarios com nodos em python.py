# Classe Funcionario
class Funcionario:
    def __init__(self, Codigo="indefinido", Nome="indefinido", Departamento="indefinido"):
        self.Nome = Nome
        self.Codigo = Codigo
        self.Departamento = Departamento

    def __repr__(self):
        return '%s -> %s -> %s' % (self.Codigo, self.Departamento, self.Nome)

# Classe Nodo (nó)
class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.conteudo = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.conteudo, self.proximo)

# Classe Lista Encadeada
class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def __repr__(self):
        return "[" + str(self.inicio) + "]"

    def ListaVazia(self):
        return self.inicio is None

    def ImprimeLista(self):
        atual = self.inicio
        cont = 0
        print("Inicio da Lista")
        if self.inicio is None:
            print("Lista Vazia")
        else:
            while atual is not None:
                print("Posição:", cont, atual.conteudo)
                cont += 1
                atual = atual.proximo
        print("Final da Lista")

    def Numero_Funcionarios(self):
        tamanho = 0
        atual = self.inicio
        while atual is not None:
            tamanho += 1
            atual = atual.proximo
        return tamanho

    def NovoFuncionario(self, func):
        novo_nodo = Nodo(func, self.inicio)
        self.inicio = novo_nodo

    def Remove_Funcionario(self, func):
        atual = self.inicio
        anterior = None

        while atual is not None:
            if atual.conteudo == func:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return
            anterior = atual
            atual = atual.proximo

# Programa principal de teste
lista = ListaEncadeada()

F1 = Funcionario("Ad01", "João", "Eletronicos")
F2 = Funcionario("Ad02", "Maria", "Eletronicos")
F3 = Funcionario("Ad03", "Jose", "Eletronicos")
F4 = Funcionario("Ad04", "Lucas", "Eletronicos")
F5 = Funcionario("Ad05", "Rodrigo", "Eletronicos")

lista.NovoFuncionario(F1)
lista.NovoFuncionario(F2)
lista.NovoFuncionario(F3)
lista.NovoFuncionario(F4)
lista.NovoFuncionario(F5)

lista.ImprimeLista()
print("Total de funcionarios na empresa:", lista.Numero_Funcionarios())

lista.Remove_Funcionario(F3)
lista.ImprimeLista()
print("Total de funcionarios na empresa:", lista.Numero_Funcionarios())

lista.Remove_Funcionario(F5)
lista.ImprimeLista()
print("Total de funcionarios na empresa:", lista.Numero_Funcionarios())
