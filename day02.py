#Desafio: Permitir armazenar várias tarefas em uma lista.

#1° pede as tarefas ao usuário:
#tarefa1 = input("Digite a primeira tarefa: ")
#tarefa2 = input("Digite a segunda tarefa: ")
#tarefa3 = input("Digite a terceira tarefa: ")

#2° Cria variavel lista com todas tarefas armazenadas:
#lista_tarefas = [tarefa1, tarefa2, tarefa3]

#3° lista as tarefas:
#print(lista_tarefas)

#cria a variavel quantidade para receber um número de tarefas
quantidade = int(input("Quantas tarefas você quer adicionar? "))

#lista vazia para armazenar tarefas
lista_tarefas = []

# usa um loop for para repetir a entrada de dados "quantidade" de vezes 
for i in range(quantidade):
    tarefa = input(f"Digite a tarefa {i + 1}: ")
    lista_tarefas.append(tarefa)

# percorre a lista de tarefas com enumerate, que retorna (índice, valor)
# start=1 faz a contagem começar em 1 em vez de 0
print("Lista de Tarefas:")
for i, tarefa in enumerate(lista_tarefas, start=1):
    print(f"{i}. {tarefa}")