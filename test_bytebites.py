from models import FoodItem, Menu, Transaction


def test_calculate_total_with_multiple_items():
    burger = FoodItem("Spicy Burger", 10.00, "Main", 4.7)
    soda = FoodItem("Large Soda", 5.00, "Drinks", 4.2)

    order = Transaction()
    order.add_item(burger)
    order.add_item(soda)

    assert order.calculate_total() == 15.00


def test_order_total_is_zero_when_empty():
    order = Transaction()
    assert order.calculate_total() == 0


def test_filter_menu_items_by_category():
    burger = FoodItem("Spicy Burger", 10.00, "Main", 4.7)
    soda = FoodItem("Large Soda", 5.00, "Drinks", 4.2)
    cake = FoodItem("Chocolate Cake", 6.00, "Desserts", 4.8)

    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(cake)

    drinks = menu.filter_by_category("Drinks")

    assert len(drinks) == 1
    assert drinks[0].name == "Large Soda"