import json
from database import ContactDatabase

class ContactBook():


        def add_contacts():

            name = input("Enter your name: ")
            phone_number = input("Enter your Phone Number: ")
            
            ContactDatabase.add_database(name.strip().capitalize(),phone_number.strip())

        def display_contacts():
            contact_info = ContactDatabase.database_display()

            for contact in contact_info:
                print(contact)
            print("Contact info displayed successfully!")

        def search_contacts(contact_search):

            name = input(str("Search by name: "))
            for line in contact_search:
                if line == name.capitalize():
                    print("Contact Name Found:")
                    print(line)
            if line != name:
                print("Contact Name does not exists")

        def delete_contacts(contacts):

            name = input("Delete by name: ")

            for contact in contacts:
                if contact == name.capitalize():
                   ContactDatabase.database_delete(name.capitalize().strip())
            if contact != name:
                print("Contact name does not exists!")
                

        def main(self):

            contacts = ContactDatabase.database_search()

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

