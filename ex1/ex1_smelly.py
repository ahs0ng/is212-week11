class OrderProcessor:
    def process_order(self, order):
        self.validation(order)
        self.apply_discounts(order)
        self.update_inventory(order)
        return self.generate_reciept(order, self.total_prices(order))
    
    def validation(self, order):
        # Step 1: Validate order details
        if not order.get("customer_id"):
            raise ValueError("Customer ID is required.")
        if not order.get("items"):
            raise ValueError("Order must contain items.")
    
    def total_prices(self, order):
        # Step 2: Calculate total price
        total_price = 0
        for item in order["items"]:
            total_price += item["price"] * item["quantity"]
        return total_price
    
    def apply_discounts(self, order):
            # Step 3: Apply discounts if applicable
        if order.get("discount_code") == "SUMMER20":
            total_price *= 0.8  # 20% discount
        elif order.get("discount_code") == "WELCOME10":
            total_price *= 0.9  # 10% discount

    def update_inventory(self, order):
        # Step 4: Update inventory
        for item in order["items"]:
            item_name = item["name"]
            item_quantity = item["quantity"]
            print(f"Updating inventory for {item_name}: -{item_quantity} units")
            
    def generate_reciept(self, order, total_price):
        # Step 5: Generate receipt
        receipt = {
            "customer_id": order["customer_id"],
            "total_price": total_price,
            "items": order["items"],
            "discount": order.get("discount_code"),
        }
        return receipt
