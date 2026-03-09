I'll create a short todo plan and mark the work done.

Created 2 todos

UML-style class diagram (text)

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

Menu 1 --- * FoodItem (Menu contains many FoodItems)
Transaction * --- * FoodItem (Transaction includes one or more FoodItems)
Customer 1 --- * Transaction (Customer has zero or more Transactions as purchaseHistory)
Notes:

totalCost in Transaction is derived by summing price of each FoodItem in items.
No extra classes were added; design kept minimal per spec.