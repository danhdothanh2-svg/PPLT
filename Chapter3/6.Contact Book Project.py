def add_contact(contact_list):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contact = f"{name} - {phone}"
    contact_list.append(contact)
    print("Contact added successfully!\n")

def show_contacts(contact_list):
    if not contact_list:
        print("No contacts yet.\n")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contact_list, start=1):
            print(f"{i}. {contact}")
        print()

def search_contact(contact_list):
    search_name = input("Enter name to search: ")
    found = False

    for contact in contact_list:
        if search_name.lower() in contact.lower():
            print("Found:", contact)
            found = True
    if not found:
        print("Not found.")
    print()

def main():
    my_contacts = []

    while True:
        print("==== CONTACT MANAGEMENT SYSTEM ====")
        print("1. Add new contact")
        print("2. Display all contacts")
        print("3. Search contact")
        print("4. Exit program")
        print("===================================")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_contact(my_contacts)
        elif choice == '2':
            show_contacts(my_contacts)
        elif choice == '3':
            search_contact(my_contacts)
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run program
main()