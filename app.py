import os

restaurantes = ['Habibs', 'MacDonalds', 'Restaurante Dona Maria']

def exibir_nome_do_programa():
    print("Sabor Express")

def exibir_opcoes():
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Sair\n")

def finalizar_app():
    os.system('cls')
    print("Saindo da aplicação...\n")

def opcao_invalida():
    print("Opção inválida!\n")
    input("Por favor aperte qualquer tecla e selecione uma opção válida!")
    main()

def seleciona_opcao_cadastro():
    opcao = int(input(""))

    if (opcao == 1):
        cadastrar_novo_restaurante()
    elif (opcao == 2):
        main()
    elif (opcao == 3):
        finalizar_app()
    else: 
        opcao_invalida()

def cadastrar_novo_restaurante():
    os.system('cls')
    print("Cadastro de novos restaurantes\n")
    nome_restaurante = input("Informe o nome do reaurante que deseja cadastrar: ")
    os.system('cls')
    restaurantes.append(nome_restaurante)
    print(f"O estabelecimento {nome_restaurante} foi inserido com sucesso!\n")

    print("1. Inserir novo restaurante?")
    print("2. Voltar ao menu principal")
    print("3. Sair\n")

    seleciona_opcao_cadastro()

def listar_restaurantes():
    os.system('cls')
    print("Listando Restaurantes\n")

    

    print("1. Inserir novo restaurante?")
    print("2. Voltar ao menu principal")
    print("3. Sair\n")

    seleciona_opcao_cadastro()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        ## print(f"Você escolheu a opção: {opcao_escolhida} ")

        if (opcao_escolhida == 1):
            cadastrar_novo_restaurante()
        elif (opcao_escolhida == 2):
            listar_restaurantes()
        elif (opcao_escolhida == 3):
            print("Cadastrar restaurante")
        elif (opcao_escolhida == 4):
            finalizar_app()
        else:
            opcao_invalida()
    except:
            opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__': 
    main()