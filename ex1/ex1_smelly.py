class OrderProcessor:
    def process_order(self, order):
        self._validate_order(order)
        total_price = self._calculate_total_price(order)
        total_price = self._apply_discount(order, total_price)
        self._update_inventory(order)
        receipt = self._generate_receipt(order, total_price)
        self._send_confirmation_email(order, receipt)
        return receipt

    def _validate_order(self, order):
        """Validate order details."""
        if not order.get("customer_id"):
            raise ValueError("Customer ID is required.")
        if not order.get("items"):
            raise ValueError("Order must contain items.")

    def _calculate_total_price(self, order):
        """Calculate total price from order items."""
        total_price = 0
        for item in order["items"]:
            total_price += item["price"] * item["quantity"]
        return total_price

    def _apply_discount(self, order, total_price):
        """Apply discount code if applicable."""
        if order.get("discount_code") == "SUMMER20":
            total_price *= 0.8  # 20% discount
        elif order.get("discount_code") == "WELCOME10":
            total_price *= 0.9  # 10% discount
        return total_price

    def _update_inventory(self, order):
        """Update inventory for each item in the order."""
        for item in order["items"]:
            item_id = item["id"]
            quantity = item["quantity"]
            # Code to update inventory for each item
            # (for simplicity, let's assume a simple print statement here)
            print(f"Updating inventory for item {item_id}, reducing stock by {quantity}.")

    def _generate_receipt(self, order, total_price):
        """Generate receipt for the order."""
        receipt = f"Customer ID: {order['customer_id']}\n"
        receipt += "Items:\n"
        for item in order["items"]:
            receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
        receipt += f"Total: ${total_price:.2f}\n"
        return receipt

    def _send_confirmation_email(self, order, receipt):
        """Send confirmation email to customer."""
        print(f"Sending email to customer {order['customer_id']} with receipt:\n{receipt}")

