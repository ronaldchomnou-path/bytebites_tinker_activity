# ByteBites core classes:
# Customer - stores customer name and purchase history
# FoodItem - stores item name, price, category, and popularity rating
# Menu - stores a collection of food items and allows filtering by category
# Transaction - stores selected items and calculates the total cost


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_purchase(self, transaction):
        self.purchase_history.append(transaction)


class FoodItem:
    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def __repr__(self):
        return f"{self.name} (${self.price})"


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def filter_by_category(self, category):
        return [item for item in self.items if item.category.lower() == category.lower()]

    def sort_by_popularity(self):
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)


class Transaction:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)


# Quick manual test
if __name__ == "__main__":
    burger = FoodItem("Spicy Burger", 10.99, "Main", 4.7)
    soda = FoodItem("Large Soda", 2.99, "Drinks", 4.2)
    cake = FoodItem("Chocolate Cake", 5.49, "Desserts", 4.8)

    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(cake)

    print("Filtered Drinks:")
    print(menu.filter_by_category("Drinks"))

    print("\nSorted by popularity:")
    print(menu.sort_by_popularity())

    order = Transaction()
    order.add_item(burger)
    order.add_item(soda)

    print("\nOrder total:")
    print(order.calculate_total())