# Menu Driven Program for List Operations

my_list = []

while True:
    print("\n----- MENU -----")
    print("1. Create List")
    print("2. Display List")
    print("3. Add Element")
    print("4. Remove Element")
    print("5. Search Element")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        n = int(input("How many elements? "))
        my_list = []
        for i in range(n):
            element = input("Enter element: ")
            my_list.append(element)
        print("List created successfully!")

    elif choice == 2:
        print("Current List:", my_list)

    elif choice == 3:
        element = input("Enter element to add: ")
        my_list.append(element)
        print("Element added successfully!")

    elif choice == 4:
        element = input("Enter element to remove: ")
        if element in my_list:
            my_list.remove(element)
            print("Element removed successfully!")
        else:
            print("Element not found!")

    elif choice == 5:
        element = input("Enter element to search: ")
        if element in my_list:
            print("Element found at index:", my_list.index(element))
        else:
            print("Element not found!")

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 9.")
