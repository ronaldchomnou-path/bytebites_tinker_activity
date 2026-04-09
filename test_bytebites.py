import pytest
from models import Customer, FoodItem, Menu, Transaction


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


def test_sort_menu_items_by_popularity():
    burger = FoodItem("Spicy Burger", 10.00, "Main", 4.7)
    soda = FoodItem("Large Soda", 5.00, "Drinks", 4.2)
    cake = FoodItem("Chocolate Cake", 6.00, "Desserts", 4.8)

    menu = Menu()
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(cake)

    sorted_items = menu.sort_by_popularity()

    assert sorted_items[0].name == "Chocolate Cake"  # highest rating 4.8
    assert sorted_items[-1].name == "Large Soda"     # lowest rating 4.2


def test_customer_purchase_history():
    customer = Customer("Alice")
    transaction1 = Transaction()
    transaction2 = Transaction()

    burger = FoodItem("Spicy Burger", 10.00, "Main", 4.7)
    transaction1.add_item(burger)

    soda = FoodItem("Large Soda", 5.00, "Drinks", 4.2)
    transaction2.add_item(soda)

    customer.add_purchase(transaction1)
    customer.add_purchase(transaction2)

    assert len(customer.purchase_history) == 2
    assert customer.purchase_history[0].items[0].name == "Spicy Burger"


def test_filter_empty_category_returns_empty_list():
    menu = Menu()
    results = menu.filter_by_category("NonExistentCategory")
    assert results == []


def test_fooditem_negative_price_raises():
    with pytest.raises(ValueError):
        FoodItem("Invalid Item", -1.00, "Main", 3.0)


def test_transaction_clear_items():
    transaction = Transaction()
    burger = FoodItem("Spicy Burger", 10.00, "Main", 4.7)
    transaction.add_item(burger)
    transaction.clear()
    assert len(transaction.items) == 0
    assert transaction.calculate_total() == 0