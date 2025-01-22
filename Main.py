import json
from database import ContactDatabase

class ContactBook():


        def add_contacts():

            name = input("Enter your name: ")
            phone_number = input("Enter your Phone Number: ")
            
            ContactDatabase.add_database(name,phone_number)

        def display_contacts():

            contact_info = ContactDatabase.database_display()

            for contact in contact_info:
                print(contact)

        def search_contacts():

            contact_search = ContactDatabase.database_search()

            name = input("Search by name: ")
            for line in contact_search:
                if line == name:
                    print("Contact Name Found:")
                    print(line)
            if line != name:
                print("Contact Name does not exists")

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
                        ContactBook.add_contacts()
                        break
                    case 2: 
                        ContactBook.display_contacts()
                        break
                    case 3:
                        ContactBook.search_contacts()
                        break
                    case 4:
                        ContactBook.delete_contacts()
                        break
                    case 5:
                        break
                    case _:
                        print("Invalid Input!")

contact = ContactBook()
contact.main()

