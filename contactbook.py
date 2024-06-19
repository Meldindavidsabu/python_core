
print("1. Add a contact ") 
print("2. Delete a contact") 
print("3. Edit a contact ")
print("4. Search a contact") 
print("5. List all contacts") 
print("6. Exit")

contactbook = {}
choice = int(input("Enter your choice "))

while choice != 6:
    if choice == 1:
        name = input("Enter the name: ")
        phno = int(input("Enter the phone number: "))
        contactbook[name] = phno
        print("1 contact added successfully")

    elif choice == 2:
        name = input("Enter the name of contact to delete: ")
        if name in contactbook:
            contactbook.pop(name)
            print("1 contact deleted successfully")
        else:
            print("Contact not found!")

    elif choice == 3:
        name = input("Enter the name of contact to edit: ")
        phno = int(input("Enter the new phone number: "))
        if name in contactbook:
            contactbook[name] = phno
            print("Contact edited successfully")
        else:
            print("Contact not found!")

    elif choice == 4:
        name = input("Enter the name: ")
        if name in contactbook:
            print("Phone Number of", name, ":", contactbook[name])
        else:
            print("Contact not found!")

    elif choice == 5:
        print("Name\t\tPhone Number")
        for x, y in contactbook.items():
            print(x, "\t\t", y)

    else:
        print("Invalid choice !!!")

    choice = int(input("Enter your choice "))

print("Exiting the contact book application")

