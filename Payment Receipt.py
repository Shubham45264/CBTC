class items:
    def __init__(self, id, itemName, price): 
        self.id = id
        self.itemName = itemName 
        self.price = price


def display(l, cName, cAddress): 
    total = 0
    print("\n\n\n")
    print("\t    Shubham Shop   ")
    print("\t  ---------------- ")
    print(f"Name: {cName} \t Address : {cAddress}\n")
    for obj in l:
        print(f"Id : {obj.id} \t ItemName : {obj.itemName} \t Price : {obj.price}")  # corrected variable name
        print("-------------------------------------------------")
        total += obj.price
    print(f"\t\tTotal : {total}") 
    print("\n")
    print("\tThanks for visiting ")
    print("\n\n")


print("\n\n")
print("Hello Everyone........")
cName = input("Enter your name   ")
cAddress = input("Enter your address   ")
totalItems = int(input("Enter the total items   "))
print("\n")

list = []

for i in range(0, totalItems):
    id = (i + 1)
    name = input("Enter item name    ")
    price = int(input("Enter price    "))
    list.append(items(id, name, price))

display(list, cName, cAddress)
