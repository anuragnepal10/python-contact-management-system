import csv
from datetime import datetime
import os

CENTER = 110
FILE_NAME = "contacts.csv"
fieldnames = ["Name","Phone Number","Created on"]
TABLE_END = "\t\t\t"

iter_dict = {
    "create":"Create another contact",
    "search":"Search another contact",
    "edit":"Edit another contact",
    "delete":"Delete another contact"
}


def iter(key):
    value = iter_dict[key]
    print()
    print(f"{value}?\nPress 'y' to {value.lower()},\nPress 'Enter' to return on Main Menu.")
    replay = input("").lower()

    if replay!="y":
        return False
    else:
        return True


def title():
    os.system("cls")
    print(("-"*35).center(CENTER))
    print("CONTACT MANAGEMENT SYSTEM".center(CENTER))
    print(("-"*35).center(CENTER))
    print("\n")

class ContactLibrary:

    def main_menu(self):
        title()
        print('''
    1. View Contact
    2. Search Contact
    3. Create Contact
    4. Edit Contact
    5. Delete Contact
    6. Exit

        ''')
    
    def create_contact(self):
        title()        
        while True:
            duplicate = False
            name = input("Enter Name: ").title()
            with open(FILE_NAME,"r") as f:
                f_reader = csv.reader(f)
                for item in f_reader:
                    if name == item[0]:
                        print("Duplicate Entry Not Allowed".center(CENTER))
                        duplicate = True
                        break
                if not duplicate:
                    break
                       
        
        phone = input("Enter Phone Number: ")
        date = datetime.now().strftime("%I:%M %p - %b %d, %Y")
        entry_list = [name,phone,date]
        
        with open(FILE_NAME,"a",newline="") as f:
            f_appender = csv.writer(f)
            f_appender.writerow(entry_list)
        
        entry_list =[]
        print("Contact created Successfully.".center(CENTER))

    def view_contact(self):
        title()
        
        data = []
        
        if os.path.getsize(FILE_NAME) == 0:
            print("Contact List is Empty".center(CENTER))
        else:
            with open (FILE_NAME,"r") as f:
                f_reader = csv.reader(f)
                for item in f_reader:
                    data.append(item)
                total_contacts = len(data)
                print(f"Total Contacts: {total_contacts}\n")
            
            for index,item in enumerate(fieldnames):
                if index!=(len(fieldnames)-1):
                    print(f"{item:30s}",end=TABLE_END)
                else:
                    print(f"{item:30s}")
            print("_"*120)
            print()
            for index,item in enumerate(data):
                for subitem in item:
                    print(f"{subitem:30s}",end=TABLE_END)
                print()
            print()
        _ = input()

    def edit_contact(self):
        title()
        to_edit = input("Enter Name of the contact you wish to edit: ").title()
        
        found = False
        ml = []
        with open (FILE_NAME,"r") as f:
            f_reader = csv.reader(f)
            for item in f_reader:
                if item[0] == to_edit:
                    print()
                    print("Skip any field to unchange previous value.")
                    name = input("Edit Name: ").title()
                    if name == "":
                        name = item[0]
                    phone = input("Edit Phone Number: ")
                    if phone == "":
                        phone = item[1]
                    
                    item [0] = name
                    item [1] = phone
                    
                    print ("\nContact Edited Successfully.".center(CENTER))
                    found = True

                ml.append(item)
        if found:
            with open ("contacts.csv","w",newline="") as f:
                f_writer = csv.writer(f)
                f_writer.writerows(ml)
        else:
            print()
            print("Contact Unavailable".center(CENTER))
           
    def delete_contact(self):
        title()
        print("Enter 'delete all' to clear all from Contact Lists,")
        name = input("Enter Name you wish to delete from Contact Lists: ")
        
        if name != "delete all":
            name = name.title()
            found = False
            ml = []
            
            with open(FILE_NAME,"r") as f:
                f_reader = csv.reader(f)
                for item in f_reader:
                    if name != item[0]:
                        ml.append(item)
                    else:
                        found = True
            print()                    
            if not found:
                print("Contact Unavailable".center(CENTER))
            else:    
                with open(FILE_NAME,"w",newline="") as f:
                    f_writer = csv.writer(f)
                    f_writer.writerows(ml)
                    print("Contact Deleted Successfully".center(CENTER))
        else:
            with open(FILE_NAME,"w",newline="") as f:
                pass
            print()
            print ("All Contacts Removed from Contact Lists Successfully".center(CENTER))

    def search_contact(self):
        
        title()
        name = input("Search Name: ").title()
        found = False
        search = []
        with open(FILE_NAME,"r") as f:
            f_reader = csv.reader(f)
            for item in f_reader:
                if name == item[0]:
                    search = item[:]
                    found = True
        print()
        if found:
            print (f"Name: {search[0]}")
            print (f"Phone Number: {search[1]}")
            print (f"Created on: {search[2]}")
        else:
            print ("Contact Unavailable".center(CENTER))

    def exit_contact(self):
        title()    
        print("Thank You. Visit Again !!".center(CENTER),end="")
        _ = input()
        exit()





def main():
    contact = ContactLibrary()
    while True:
        contact.main_menu()
        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:
            contact.view_contact()
        
        elif user_choice == 2:
            while True:
                contact.search_contact()
                if not iter("search"):
                    break

        elif user_choice == 3:
            
            while True:
                contact.create_contact()
                if not iter("create"):
                    break

        
        elif user_choice == 4:
            
            while True:
                contact.edit_contact()
                if not iter("edit"):
                    break
        
        elif user_choice == 5:
            
            while True:
                contact.delete_contact()
                if not iter("delete"):
                    break

        elif user_choice == 6:

            contact.exit_contact()
            

if __name__ == "__main__":
    main()