import sqlite3

def criar_tabela():
    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()

    # Criação da tabela se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            area_estudo TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def incluir_aluno():
    nome = input("Digite o nome do aluno: ")
    area_estudo = input("Digite a área de estudo do aluno: ")

    conn = sqlite3.connect('alunos.db')
    cursor = conn.cursor()

    # Inserção de um novo aluno
    cursor.execute('''
        INSERT INTO alunos (nome, area_estudo) VALUES (?, ?)
    ''', (nome, area_estudo))

    conn.commit()
    conn.close()

# Criar a tabela (execute isso uma vez para inicializar o banco de dados)
criar_tabela()

# Incluir novos alunos
incluir_aluno()

print("Aluno incluído com sucesso!")


def busca_sequencial_banco(chave):
    conn = sqlite3.connect('alunos.db')  # Conectar ao banco de dados
    cursor = conn.cursor()

    # Executar a consulta
    cursor.execute('SELECT area_estudo FROM alunos WHERE nome = ?', (chave,))
    resultado = cursor.fetchone()

    # Fechar a conexão
    conn.close()

    if resultado:
        return resultado[0]
    else:
        return "Aluno não encontrado"

# Exemplo de utilização
chave = input("Digite o nome de um aluno para pesquisa: ")
resultado = busca_sequencial_banco(chave)
print(resultado)
