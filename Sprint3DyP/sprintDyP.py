# Tabela de pontuações e nomes dos alunos
tabela_pontuacoes = [
    ["João Pedro", 85, 90, 78],
    ["Gabriel Garcia", 88, 92, 80]
]

# Função para adicionar uma pontuação ao aluno na tabela
def adicionar_pontuacao(tabela, nome_aluno, pontuacao):
    for linha in tabela:
        if linha[0] == nome_aluno:
            linha.append(pontuacao)
            return
    # Se o aluno não existir, cria uma nova linha para ele

    tabela.append([nome_aluno, pontuacao])
# Função para exibir as pontuações de um aluno
def exibir_pontuacoes(tabela, nome_aluno):
    for linha in tabela:
        if linha[0] == nome_aluno:
            pontuacoes = linha[1:]  # Mostra todas as pontuações do aluno
            return f"A pontuação do aluno {nome_aluno} é: {pontuacoes}"
    return "Aluno não encontrado"

# Adicionando novas pontuações a tabela
adicionar_pontuacao(tabela_pontuacoes, "João Pedro", 95)
adicionar_pontuacao(tabela_pontuacoes, "Miguel Gonçalves", 100)  # Criando um novo aluno e adicionando a tabela

# Exibindo pontuações e nome dos alunos
print(exibir_pontuacoes(tabela_pontuacoes, "João Pedro"))        
print(exibir_pontuacoes(tabela_pontuacoes, "Gabriel Garcia"))    
print(exibir_pontuacoes(tabela_pontuacoes, "Miguel Gonçalves"))  
