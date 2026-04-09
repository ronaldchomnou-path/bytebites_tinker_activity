from decimal import Decimal


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.purchase_history = []

    def add_purchase(self, transaction):
        self.purchase_history.append(transaction)

    def __repr__(self):
        return f"Customer(name={self.name}, purchases={len(self.purchase_history)})"


class FoodItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.name = name
        self.price = float(price)
        self.category = category
        self.popularity_rating = float(popularity_rating)

    def __repr__(self):
        return f"{self.name} (${self.price:.2f})"


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item: FoodItem):
        self.items.append(item)

    def filter_by_category(self, category: str):
        return [item for item in self.items if item.category.lower() == category.lower()]

    def sort_by_popularity(self):
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)

    def __repr__(self):
        return f"Menu({len(self.items)} items)"


class Transaction:
    def __init__(self):
        self.items = []

    def add_item(self, item: FoodItem):
        self.items.append(item)

    def calculate_total(self):
        # Using Decimal for more precise currency calculation
        total = sum(Decimal(f"{item.price}") for item in self.items)
        return float(total)

    def clear(self):
        self.items.clear()

    def __repr__(self):
        return f"Transaction({len(self.items)} items, total=${self.calculate_total():.2f})"


# Quick manual test snippet
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