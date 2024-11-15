import json

file_path = "contacts.json"


def load_contacts(file_path = "contacts.json"):
    try:
        with open(file_path, "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = []
    except json.JSONDecodeError:
        print("Error Reading Contacts. Starting with empty contact lists")
        contacts = []
    return contacts

def add_contacts(contacts, file_path):
    name = input("Enter your name: ")
    phone_number = input("Enter your Phone Number: ")
    
    details = {"name":name, "phone":phone_number}
    contacts.append(details)

    try:
        with open(file_path, "w") as file:
            json.dump(contacts, file)
    except IOError:
        print("Error Saving Contacts")
    print("Contact Infomration Added Successfully!")

def display_contacts(contacts):
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")


def main():
    contacts = load_contacts()
    while True:
        print("Choose your transaction: ")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Exit")
        choice = int(input("Enter here: "))

        match choice:
            case 1: 
                add_contacts(contacts,file_path)
            case 2: 
                display_contacts(contacts)
            case 3:
                break
            case _:
                print("Invalid Input!")

main()

