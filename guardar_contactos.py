# === GUARDAR CONTACTOS NUM FICHEIRO À PARTE ===

def adicionar_contacto():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    data_nasce = input("Digite a data de nascimento: ")
    email = input("Digite o email do contato: ")

    with open("contatos.txt", "a") as arquivo:
        arquivo.write(f"Nome: {nome},Data Nascimento: {data_nasce}, Telefone: {telefone}, Email: {email}\n")
    print("Contato adicionado com sucesso!")

def mostrar_contactos():

    try:
        with open("contatos.txt", "r") as arquivo:
            print("=== Contatos ===")
            for linha in arquivo:
                print(linha.strip())  # Remove espaços em branco extras
    except FileNotFoundError:
        print("Nenhum contato encontrado.")

def apagar_contactos():
    nome = input("Digite o nome do contato que deseja apagar: ")

    with open("contatos.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("contatos.txt", "w") as arquivo:
        for linha in linhas:
            if nome not in linha:
                arquivo.write(linha)
    print("Contato apagado com sucesso!")
    

def main():
    while True:
        print("\n=== MENU ===")
        print("1 - Adicionar Contato")
        print("2 - Mostrar contactos")
        print("3 - Apagar contacto")
        print("4 - sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_contacto()
        elif escolha == "4":
            print("Saindo do programa...")
            break
        elif escolha == "2":
            mostrar_contactos()

        elif escolha == "3":
            ()

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
