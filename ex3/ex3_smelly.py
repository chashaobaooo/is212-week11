class Product:
    """Base class for all products with common functionality."""
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_discount_rate(self):
        """Override this method in subclasses to specify discount rate."""
        raise NotImplementedError("Subclasses must implement get_discount_rate()")
    
    def get_tax_rate(self):
        """Override this method in subclasses to specify tax rate."""
        raise NotImplementedError("Subclasses must implement get_tax_rate()")
    
    def get_category_name(self):
        """Override this method in subclasses to specify category name."""
        raise NotImplementedError("Subclasses must implement get_category_name()")
    
    def apply_discount(self):
        """Calculate and return discounted price."""
        discount = self.get_discount_rate()
        discounted_price = self.price - (self.price * discount)
        print(f"Discounted price for {self.name} ({self.get_category_name()}): {discounted_price}")
        return discounted_price
    
    def calculate_tax(self):
        """Calculate and return tax amount."""
        tax_rate = self.get_tax_rate()
        tax = self.price * tax_rate
        print(f"Tax for {self.name} ({self.get_category_name()}): {tax}")
        return tax


class Electronics(Product):
    def get_discount_rate(self):
        return 0.10  # 10% discount
    
    def get_tax_rate(self):
        return 0.15  # 15% tax
    
    def get_category_name(self):
        return "Electronics"


class Clothing(Product):
    def get_discount_rate(self):
        return 0.20  # 20% discount
    
    def get_tax_rate(self):
        return 0.08  # 8% tax
    
    def get_category_name(self):
        return "Clothing"


class Grocery(Product):
    def get_discount_rate(self):
        return 0.05  # 5% discount
    
    def get_tax_rate(self):
        return 0.02  # 2% tax
    
    def get_category_name(self):
        return "Grocery"

