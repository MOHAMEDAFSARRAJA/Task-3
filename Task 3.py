import os

FILE_NAME = 'contacts.txt'


def display_menu():

    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Delete Contact")
    print("4. Exit")


def add_contact():

    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")

    with open(FILE_NAME, 'a') as file:
        file.write(f"{name},{phone}\n")

    print("Contact added successfully!")


def view_contacts():

    if not os.path.exists(FILE_NAME):
        print("No contacts found.")
        return

    with open(FILE_NAME, 'r') as file:
        contacts = file.readlines()

    if contacts:
        print("\nContacts List:")
        for contact in contacts:
            name, phone = contact.strip().split(',')
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("No contacts found.")


def delete_contact():

    if not os.path.exists(FILE_NAME):
        print("No contacts found.")
        return

    name_to_delete = input("Enter the name of the contact to delete: ")

    with open(FILE_NAME, 'r') as file:
        contacts = file.readlines()

    with open(FILE_NAME, 'w') as file:
        found = False
        for contact in contacts:
            name, phone = contact.strip().split(',')
            if name != name_to_delete:
                file.write(contact)
            else:
                found = True

    if found:
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def main():

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
