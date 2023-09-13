shopList = []
item = str(input("Enter items in the shopping list: "))

while item.lower() != 'done':
    shopList.append(item)
    item = str(input("Enter items in the shopping list: "))

for i, value in enumerate(shopList, start=1):
    print(f"{i}: {value}")