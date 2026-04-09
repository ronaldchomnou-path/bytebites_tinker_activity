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

Customer 1 --- * Transaction  (Customer can have multiple Transactions)
Transaction * --- * FoodItem  (Transaction contains one or more FoodItems)
Menu 1 --- * FoodItem         (Menu contains multiple FoodItems)

totalCost is derived by summing each FoodItem.price in Transaction.items.
Design is minimal and follows the ByteBites spec; no extra classes added.