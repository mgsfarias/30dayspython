#Desafio: Salvar tarefas em um arquivo .txt e carregá-las ao iniciar o programa.

import os

# Lista que irá armazenar as tarefas
tarefas = []

# Nome do arquivo onde vamos salvar as tarefas
ARQUIVO = "tarefas.txt"

# Função para carregar tarefas do arquivo ao iniciar o programa
def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                titulo, status = linha.strip().split(" | ")
                tarefas.append({"titulo": titulo, "status": status})

# Função para salvar tarefas no arquivo
def salvar_tarefas():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"{tarefa['titulo']} | {tarefa['status']}\n")

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    while True:
        titulo = input("\nDigite o título da tarefa: ").strip()
        
        if titulo == "" or titulo.isdigit():
            print("Tarefa inválida. Não pode estar vazia nem ser apenas números.")
            continue
        
        tarefa = {"titulo": titulo, "status": "pendente"}
        tarefas.append(tarefa)
        salvar_tarefas()  # salva após cada alteração
        print(f"\nTarefa '{titulo}' adicionada com sucesso!")
        break

# Função para listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("\nNenhuma tarefa foi cadastrada ainda.")
        return
    
    print("\n======= Lista de Tarefas =======")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i:02d}. {tarefa['titulo']} --> Status: [{tarefa['status']}]")
    print("================================")

# Função para concluir uma tarefa
def concluir_tarefa():
    if not tarefas:
        print("\nNenhuma tarefa para concluir.")
        return
    
    listar_tarefas()
    
    while True:
        escolha = input("\nDigite o número da tarefa a concluir (ou 'c' para cancelar): ").strip()
        
        if escolha.lower() == "c":
            print("Operação cancelada.")
            return
        
        if not escolha.isdigit():
            print("Digite um número válido ou 'c' para cancelar.")
            continue
        
        indice = int(escolha) - 1
        
        if indice < 0 or indice >= len(tarefas):
            print("Número fora do intervalo. Tente novamente.")
            continue
        
        if tarefas[indice]["status"] == "concluída":
            print("Essa tarefa já estava concluída.")
            return
        
        tarefas[indice]["status"] = "concluída"
        salvar_tarefas()  # salva alteração
        print(f"Tarefa '{tarefas[indice]['titulo']}' marcada como concluída!")
        return

# Função principal do menu
def menu():
    carregar_tarefas()  # carrega as tarefas logo no início
    
    while True:
        print("""
======= MENU =======
1 - Adicionar tarefa
2 - Listar tarefas
3 - Concluir tarefa
4 - Sair
====================
""")
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")

# Inicia o programa
menu()
