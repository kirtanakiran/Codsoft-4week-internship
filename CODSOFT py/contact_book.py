import json

def load_contacts():
    try:
        with open('contacts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contacts(contacts):
    query = input("Enter name or phone number to search: ").lower()
    results = [contact for contact in contacts if query in contact['name'].lower() or query in contact['phone']]
    
    if results:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contacts found.")

def update_contact(contacts):
    query = input("Enter name or phone number of the contact to update: ").lower()
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print(f"Current details: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
            contact['name'] = input(f"Enter new name (or press Enter to keep '{contact['name']}'): ") or contact['name']
            contact['phone'] = input(f"Enter new phone number (or press Enter to keep '{contact['phone']}'): ") or contact['phone']
            contact['email'] = input(f"Enter new email address (or press Enter to keep '{contact['email']}'): ") or contact['email']
            contact['address'] = input(f"Enter new address (or press Enter to keep '{contact['address']}'): ") or contact['address']
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact(contacts):
    query = input("Enter name or phone number of the contact to delete: ").lower()
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contacts(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
