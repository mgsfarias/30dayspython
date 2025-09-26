# Desafio: Tratar erros ao abrir arquivos ou inserir dados inválidos.

import os

# Lista que irá armazenar as tarefas
tarefas = []

# Nome do arquivo onde vamos salvar as tarefas
ARQUIVO = "tarefas.txt"

# Função para carregar tarefas do arquivo ao iniciar o programa
def carregar_tarefas():
    if os.path.exists(ARQUIVO):  # só tenta abrir se o arquivo existir
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
                for linha in arquivo:
                    # Cada linha deve ter "titulo | status"
                    try:
                        titulo, status = linha.strip().split(" | ")
                        tarefas.append({"titulo": titulo, "status": status})
                    except ValueError:
                        # Caso o formato da linha esteja errado
                        print(f"Linha inválida ignorada: {linha.strip()}")
        except Exception as e:
            print(f"Erro ao carregar o arquivo: {e}")

# Função para salvar tarefas no arquivo
def salvar_tarefas():
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            for tarefa in tarefas:
                arquivo.write(f"{tarefa['titulo']} | {tarefa['status']}\n")
    except Exception as e:
        print(f"Erro ao salvar tarefas: {e}")

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    while True:
        titulo = input("\nDigite o título da tarefa: ").strip()
        
        # Verifica se é válido
        if titulo == "" or titulo.isdigit():
            print("Tarefa inválida. Não pode estar vazia nem ser apenas números.")
            continue
        
        tarefa = {"titulo": titulo, "status": "pendente"}
        tarefas.append(tarefa)
        
        # Tratando possível erro ao salvar
        try:
            salvar_tarefas()
            print(f"\nTarefa '{titulo}' adicionada com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar a tarefa: {e}")
        
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
        
        try:
            indice = int(escolha) - 1
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue
        
        if indice < 0 or indice >= len(tarefas):
            print("Número fora do intervalo. Tente novamente.")
            continue
        
        if tarefas[indice]["status"] == "concluída":
            print("Essa tarefa já estava concluída.")
            return
        
        tarefas[indice]["status"] = "concluída"
        try:
            salvar_tarefas()
            print(f"Tarefa '{tarefas[indice]['titulo']}' marcada como concluída!")
        except Exception as e:
            print(f"Erro ao salvar alteração: {e}")
        return

# Função principal do menu
def menu():
    carregar_tarefas()  # tenta carregar as tarefas logo no início
    
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
