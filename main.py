import json

FILE_NAME = "contacts.json"

# Function to save the cpntact to save the files
def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save contact file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)



# Function add new contact
def add_contact(contacts):
    name = input("Enter your name: ")
    phone = input("Enter phone number: ")
    email = input("Enter your email: ")
    contacts.append({"name": name, "phone":  phone, "email": email})
    print("Contact Added Succefully")
    
#Function to view all contacts
def view_contacts(contacts):
    if not contacts:
        print("No Contacts Found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f'{i}. {contact['name']} - {contact['phone']} - {contact['email']}')

#Function to search for a contact
def search_contact(contacts):
    name = input("Enter name to search: ")
    # found = [c for c in contacts if c['name'].lower() == name.lower()]
    found = []
    for c in contacts:
        if c["name"].lower() == name.lower():
            found.append(c)
            
    if found:
        for contact in found:
            print(f"{contact['name']} - {contact['phone']} - {contact['email']}")
    else:
        print("No contact Found")
        
#function to delete the contact
def delete_contact(contacts):
    name = input("Enter the name that u want delete: ")
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            contacts.pop(i)
            print("The contact has been deleted!!")
            return
        else:
            print("No contact Found with that name!!")
    
    
def main():
    contacts = load_contacts() 
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter Your Choice: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)  # Save the updated contacts to file
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
