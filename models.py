# ByteBites core classes:
# Customer - stores customer name and purchase history
# FoodItem - stores item name, price, category, and popularity rating
# Menu - stores a collection of food items and allows filtering by category
# Transaction - stores selected items and calculates the total cost


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []


class FoodItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating


class Menu:
    def __init__(self):
        self.items = []


class Transaction:
    def __init__(self):
        self.items = []
        
        
        
if __name__ == "__main__":
    burger = FoodItem("Spicy Burger", 10.99, "Main", 4.7)
    soda = FoodItem("Large Soda", 2.99, "Drinks", 4.2)

    print(burger.name)
    print(soda.category)
    
    