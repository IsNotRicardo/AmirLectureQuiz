shopList = {}


def add_item():
    product = str(input("Insert the item: "))
    amount = int(input("Insert the amount: "))

    if product in shopList:
        shopList[product] += amount
    else:
        shopList[product] = amount


def list_sum():
    print("The amount of items in your list is:", sum(shopList.values()))


def main():
    print("\n1. Add item to the list;\n"
          "2. Display the contents of the list;\n"
          "3. Sum amount of items in the list;\n"
          "4. Exit the application.\n")

    match int(input("Select your option: ")):
        case 1:
            add_item()
        case 2:
            print(shopList)
        case 3:
            list_sum()
        case 4:
            quit()
        case _:
            print("Invalid option!")

    main()


main()
