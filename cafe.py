#cafe.py
#Create menu with ≥ 4 items
#Create dictionary called stock
#create dictionary called price
#Calculate total stock worth using a for loop
#Display total stock worth
menu = ["Roti Prata", "Fried Rice", "Mee Goreng", "Laksa", "Char Kway Teow", "Chicken Rice"]

stock = {"Roti Prata" : 20,
         "Fried Rice" : 15,
         "Mee Goreng" : 7,
         "Laksa" : 5,
         "Char Kway Teow" : 7,
         "Chicken Rice" : 15
         }

price = {"Roti Prata" : 2,
         "Fried Rice" : 3,
         "Mee Goreng" : 4,
         "Laksa" : 7,
         "Char Kway Teow" : 4.5,
         "Chicken Rice" : 7
         }

print(("*"*5) + "Welcome to Nanka Nanka Restaurant" + ("*"*5))
print()
print(f"Here is the menu: \n{menu}")
print()

total_stock_worth = 0

for item in stock and price:  
    #use 'and' to ensure I am looping through both lists
    total_stock_worth = total_stock_worth + (stock[item] * price[item])
print(f"The total stock worth is ${total_stock_worth}")

