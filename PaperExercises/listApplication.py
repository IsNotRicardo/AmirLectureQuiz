genList = []


def add_item():
    genList.append(str(input("Insert item: ")))


def remove_item():
    try:
        genList.remove(str(input("Remove item: ")))
    except ValueError:
        print("Item not in list!")


while True:
    print("\n1. Add item to the list;\n"
          "2. Display the contents of the list;\n"
          "3. Remove item from the list;\n"
          "4. Quit the application.\n")

    match int(input("Select your option: ")):
        case 1:
            add_item()
        case 2:
            print("Your list is:", genList)
        case 3:
            remove_item()
        case 4:
            quit()
        case _:
            print("Invalid option!")