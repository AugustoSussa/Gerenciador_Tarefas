import sys

tarefas = []

def adicionar_tarefa():
    descricao = input("Digite a descrição da nova tarefa: ")
    tarefa_id = len(tarefas) + 1 
    tarefa = {"id": tarefa_id, "descricao": descricao, "status": "Pendente"}
    tarefas.append(tarefa)
    print(f"Tarefa {tarefa_id} adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        print("Lista de Tarefas:")
        for tarefa in tarefas:
            print(f"ID: {tarefa['id']}, Descrição: {tarefa['descricao']}, Status: {tarefa['status']}")

def marcar_concluida():
    try:
        tarefa_id = int(input("Digite o ID da tarefa para marcar como concluída: "))
        tarefa_encontrada = False
        
        for tarefa in tarefas:
            if tarefa["id"] == tarefa_id:
                if tarefa["status"] == "Concluída":
                    print(f"Tarefa {tarefa_id} já está concluída.")
                else:
                    tarefa["status"] = "Concluída"
                    print(f"Tarefa {tarefa_id} foi marcada como concluída.")
                tarefa_encontrada = True
                break
        
        if not tarefa_encontrada:
            print(f"Tarefa com ID {tarefa_id} não encontrada.")
    except ValueError:
        print("Por favor, insira um número válido para o ID.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar Nova Tarefa")
        print("2. Listar Todas as Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_concluida()
        elif opcao == "4":
            print("Saindo do programa...")
            sys.exit()
        else:
            print("Opção inválida, por favor escolha uma opção válida.")

if __name__ == "__main__":
    menu()