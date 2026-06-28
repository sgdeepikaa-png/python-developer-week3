from utils import format_name, calculate_age

contacts = {}

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Phone")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("0. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        first = input("First Name: ")
        last = input("Last Name: ")
        email = input("Email: ").lower()
        phone = input("Phone Number: ")
        birth_year = int(input("Birth Year: "))

        contacts[email] = {
            "name": format_name(first, last),
            "phone": phone,
            "birth_year": birth_year
        }

        print("Contact Added Successfully!")

    elif choice == "2":
        email = input("Enter Email: ").lower()

        if email in contacts:
            person = contacts[email]
            print("Name :", person["name"])
            print("Phone:", person["phone"])
            print("Age  :", calculate_age(person["birth_year"]))
        else:
            print("Contact Not Found")

    elif choice == "3":
        email = input("Enter Email: ").lower()

        if email in contacts:
            phone = input("Enter New Phone Number: ")
            contacts[email]["phone"] = phone
            print("Phone Updated")
        else:
            print("Contact Not Found")

    elif choice == "4":
        email = input("Enter Email: ").lower()

        if email in contacts:
            del contacts[email]
            print("Contact Deleted")
        else:
            print("Contact Not Found")

    elif choice == "5":
        if len(contacts) == 0:
            print("No Contacts")
        else:
            for email, person in contacts.items():
                print("----------------------")
                print("Email :", email)
                print("Name  :", person["name"])
                print("Phone :", person["phone"])
                print("Age   :", calculate_age(person["birth_year"]))

    elif choice == "0":
        print("Thank You")
        break

    else:
        print("Invalid Choice")