contacts={}

def add_contact():
    name=input("Enter name: ")
    if name in contacts:
        print("Contact already exists..")
    else:
        phone=input("Enter phone: ")
        email=input("Enter email: ")

        contacts[name]=dict(phone=phone,email=email)

        print("Contact added successfully.  ")


def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name,contact in contacts.items():
            print("\n")
            print("Name: ",name)
            print("Phone: ",contact["phone"])
            print("Email: ",contact["email"])


def search_contact():
    contact_name=input("Enter name to search: ")
    found=False
    for name,contact in contacts.items():
        if name==contact_name:
            found=True
            print("\n")
            print("Contact found!!")
            print("Name: ",name)
            print("Phone: ",contact["phone"])
            print("Email: ",contact["email"])
            print("\n")
            break
    if not found:
        print("Contact not found.")


def update_contact():
    contact_name=input("Enter name to search: ")
    if contact_name in contacts:
        new_phone=input("Enter new phone: ")
        new_email=input("Enter new email: ")
        contacts[contact_name]["phone"]=new_phone
        contacts[contact_name]["email"]=new_email
        print("Contact updated successfully..")
    else:
        print("Contact not found.")


def delete_contact():
    contact_name=input("Enter contact name to delete: ")
    if contact_name in contacts:
        del contacts[contact_name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

while True:
    print("========= CONTACT ME =========")
    print("1. Add Contact.")
    print("2. View Contacts.")
    print("3. Search Contact.")
    print("4. Update Contact.")
    print("5. Delete Contact.")
    print("6. Exit.")

    user_choice=int(input("Enter your choice: "))

    while not(0<user_choice<7):
        print("Invalid Choice.")
        user_choice=int(input("Enter your choice again: "))
    match user_choice:
        case 1:
            add_contact()
        case 2:
            view_contacts()
        case 3:
            search_contact()
        case 4:
            update_contact()
        case 5:
            delete_contact()
        case 6:
            break