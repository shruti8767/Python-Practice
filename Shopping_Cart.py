#Calculate the total cost of items in a shopping cart

def calculate_total_cost(cart):
    total_cost =0
    for item in cart:
        total_cost+=item['price']*item['quantity']
    return total_cost

cart=[
    {'name':'Apple','price':0.5,'quantity':4},
    {'name':'Banana','price':0.3,'quantity':12},
    {'name':'Chiku','price':0.4,'quantity':6},
    {'name':'Cherry','price':0.9,'quantity':3},
]

total_cost=calculate_total_cost(cart)
print(total_cost)