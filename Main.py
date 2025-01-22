import json
from database import ContactDatabase

class ContactBook():
        
        def __init__(self, file_path="contacts.json"):
            self.file_path = file_path


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
            
            ContactDatabase.add_database(name,phone_number)

        def display_contacts(contacts):

            for contact in contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")
            ContactBook.main()
            

        def search_contacts(contacts):

            name = input("Search by name: ")
            for line in contacts:
                if line["name"] == name:
                    print("Contact Name Found:")
                    print(line)
                    ContactBook.main()
                else:
                    print("Contact Name does not exists")
                    ContactBook.main()

        def delete_contacts(self,contacts):

            name = input("Delete by name: ")

            for line in contacts:
                if line['name'] == name:
                    del line["name"],line["phone"]
                    delete = [line for line in contacts if line]
                    with open(self.file_path, "w") as file:
                        json.dump(delete, file)
                        contacts = []
                    print("Contact Deleted Successfully")
                    break
                    main() 
                

        def main(self):

            contacts = ContactBook.load_contacts()

            while True:

                print("Choose your transaction: ")
                print("1. Add Contact")
                print("2. View Contacts")
                print("3. Search Contact")
                print("4. Delete Contact")
                print("5. Exit")
                choice = int(input("Enter here: "))

                match choice:
                    case 1: 
                        ContactBook.add_contacts(contacts,self.file_path)
                        break
                    case 2: 
                        ContactBook.display_contacts(contacts)
                        break
                    case 3:
                        ContactBook.search_contacts(contacts)
                        break
                    case 4:
                        ContactBook.delete_contacts(contacts)
                        break
                    case 5:
                        break
                    case _:
                        print("Invalid Input!")

contact = ContactBook()
contact.main()

