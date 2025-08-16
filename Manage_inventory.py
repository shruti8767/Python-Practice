## Managing an inventory
#Use a list to manage inventory items in a store 

#Manageing a inventory
inventory=["Apple","Banana","Cherry","Watermelon","Gauva"]

#Adding a new item
inventory.append("Berry")

#Removing a item that is not in a stock
inventory.remove("Apple")

#Checking if an item is in stock
item="Orange"
if item in inventory:
    print(f"{item} are in a stock")
else:
    print(f"{item} are out of stock")

# Printing the inventory
print("Inventory Items:")
for items in inventory:
    print(f"- {items}") 