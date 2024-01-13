import os

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

def escolher_opcao():
    opcao_escolhida = int(input("Escolha uma opção: "))
    ## print(f"Você escolheu a opção: {opcao_escolhida} ")

    if (opcao_escolhida == 1):
        print("Cadastrar restaurante")
    elif (opcao_escolhida == 2):
        print("Listar restaurante")
    elif (opcao_escolhida == 3):
        print("Cadastrar restaurante")
    elif (opcao_escolhida == 4):
        finalizar_app()
    else:
        print("Opção inválida! Por favor insira uma opção correta!")

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__': 
    main()