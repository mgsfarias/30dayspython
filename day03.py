# Desafio: Validar se o usuário não insere uma tarefa vazia

# define a variavel quantidade para receber o valor inteiro com n° de tarefas:
quantidade = int(input("Quantas tarefas você quer adicionar? "))

# cria uma lista vazia que será usada para armazenar as tarefas digitadas:
tarefas = [] 

# usa um loop for para repetir a entrada de dados "quantidade" de vezes 
for i in range (quantidade): 
     # pede ao usuário para digitar a tarefa, remove espaços extras com .strip()
    tarefa = input(f"Digite a tarefa {i+1}: ").strip()
    
    # validação: enquanto a tarefa for vazia ("") ou apenas números (isdigit),
    # o programa repete a pergunta até que o usuário digite algo válido
    while tarefa == "" or tarefa.isdigit():
        print("Tarefa vazia/número não é permitida.")
        tarefa = input(f"Digite a tarefa {i+1}: ").strip()
    
    # adiciona as tarefas válidas dentro da lista de tarefas
    tarefas.append(tarefa)

# imprime uma linha em branco (\n) e o título da lista
print("\n Lista de Tarefas:")

# percorre a lista de tarefas com enumerate, que retorna (índice, valor)
# start=1 faz a contagem começar em 1 em vez de 0
for i, t in enumerate(tarefas, start=1):
    
    # exibe cada tarefa numerada
    print(f"{i}. {t}")