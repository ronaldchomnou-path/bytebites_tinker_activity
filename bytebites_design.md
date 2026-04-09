UML Diagram (text)

+-----------------------------+

Customer
- name: String
- purchaseHistory: List<Transaction>
+-----------------------------+
+----------------------------------+

FoodItem
- name: String
- price: Decimal
- category: String
- popularityRating: Integer
+----------------------------------+
+-----------------------------+

Menu
- items: List<FoodItem>
+-----------------------------+
+-----------------------------------------+

Transaction
- items: List<FoodItem>
- totalCost: Decimal (computed)
+-----------------------------------------+
Relationships:

Menu 1 --- * FoodItem (Menu contains many FoodItem)
Transaction 1 --- * FoodItem (Transaction includes one or more FoodItem)
Customer 1 --- * Transaction (Customer has zero or more Transaction in purchaseHistory)
Notes:

totalCost is derived by summing each FoodItem.price in Transaction.items.
Design is minimal and follows the ByteBites spec; no extra classes added.