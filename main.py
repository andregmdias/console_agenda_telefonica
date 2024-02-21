# contact = {"name": string, "phone": string, "email": string, "favorite": boolean}
contacts = []


def create_contact(contacts, name, phone, email, favorite):
    contacts.append({"name": name, "phone": phone, "email": email, "favorite": favorite})
    print("Contato adicionado {\"name\": %s, \"phone\": %s, \"email\": %s, \"favorite\": %s}" % (
        name, phone, email, favorite))
    return

def get_all_contacts(contacts):
    for index, contact in enumerate(contacts, start=1):
        favorite = "✓" if contact["favorite"] else " "
        print(f"{index}. [{favorite}] - Favorito - {contact["name"]} - {contact["phone"]} - {contact["email"]}")
    return

def update_contact_favorite_status(contacts, index):
    fixed_index = index - 1
    is_favorite = contacts[fixed_index]["favorite"]
    contacts[fixed_index]["favorite"] = False if is_favorite else True
    print(f"O status de favorito do {contacts[fixed_index]["name"]} foi atualizado para {contacts[fixed_index]["favorite"]}")
    return

def get_all_favorite_contacts(contacts):
    favorite_contacts = []
    for index, contact in enumerate(contacts):
        if contact["favorite"]:
            favorite_contacts.append(contact)

    for index, contact in enumerate(favorite_contacts, start=1):
        print(f"{index}. {contact["name"]} - {contact["phone"]} - {contact["email"]}")
    return

def remove_contact(contacts, index):
    fixed_index = index - 1
    contact = contacts[fixed_index]
    contacts.pop(fixed_index)
    print(f"Contato de {contact["name"]} foi removido de sua agenda!")
    return

def update_contact_data(contacts, index, name, phone, email, favorite):
    contacts[index - 1] = {"name": name, "phone": phone, "email": email, "favorite": favorite}
    print(f"Dados do contato atualizado\n\"name\": {name}, \"phone\": {phone}, \"email\": {email}, \"favorite\": {favorite}")
    return


def get_contact_by_index(contacts, index):
    return contacts[index - 1]

while True:
    print("\nMenu opções App agenda de contatos")
    print("1. Adicionar contato")
    print("2. Listar todos os contatos")
    print("3. Editar contato")
    print("4. Favoritar/desfavoritar contato")
    print("5. Listar contatos favoritados")
    print("6. Remover contato")
    print("7. Sair")

    option = input("Digite a opção: ")

    if option == "1":
        name = input("Informe o nome do contato: ")
        phone = input("Informe o telefone: ")
        email = input("Informe o email do contato: ")
        favorite = True if input("Favoritar contato ? S/N ") == "S" else False
        create_contact(contacts, name, phone, email, favorite)
    elif option == "2":
        print("\nListando todos os contatos")
        get_all_contacts(contacts)
    elif option == "3":
        print("\nListando todos os contatos")
        get_all_contacts(contacts)
        index = int(input("Informe o número do contato que deseja atualizar: "))
        old_contact = get_contact_by_index(contacts, int(index))
        name = input("Informe o novo nome do contato: ") or old_contact["name"]
        phone = input("Informe o novo telefone: ") or old_contact["phone"]
        email = input("Informe o novo email do contato: ") or old_contact["email"]
        favorite = (True if input("Favoritar contato ? S/N ") == "S" else False) or old_contact["favorite"]
        update_contact_data(contacts, index, name, phone, email, favorite)

    elif option == "4":
        get_all_contacts(contacts)
        index = input("\nEscolha o número do contato que deseja favoritar/desfavoritar: ")
        update_contact_favorite_status(contacts, int(index))
    elif option == "5":
        print("\nListando todos os contatos favoritados")
        get_all_favorite_contacts(contacts)
    elif option == "6":
        print("\nListando todos os contatos favoritados")
        get_all_favorite_contacts(contacts)
        index = input("\nInforme o número do contato que deseja remover: ")
        remove_contact(contacts, int(index))
    elif option == "7":
        print("Programa finalizado")
        break
