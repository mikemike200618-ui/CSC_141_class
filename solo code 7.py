class ProduceItem:
    """Base class for produce items"""
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_total(self):
        raise NotImplementedError("Subclasses must implement get_total()")


class ByWeightItem(ProduceItem):
    """Produce sold by the pound"""
    def __init__(self, name, price_per_lb, weight_lb):
        super().__init__(name, price_per_lb)
        self.weight_lb = weight_lb
    
    def get_total(self):
        return self.price * self.weight_lb


class ByQuantityItem(ProduceItem):
    """Produce sold per item"""
    def __init__(self, name, price_per_item, quantity):
        super().__init__(name, price_per_item)
        self.quantity = quantity
    
    def get_total(self):
        return self.price * self.quantity


class Order:
    """Manages items in an order"""
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        """Add a ProduceItem to the order"""
        self.items.append(item)
    
    def get_items(self):
        """Return list of items in the order"""
        return self.items
    
    def calculate_total(self):
        """Calculate total cost of all items"""
        return sum(item.get_total() for item in self.items)
    
    def __len__(self):
        """Return the number of items in the order"""
        return len(self.items)


class Receipt:
    """Generates cash receipts for produce purchases"""
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def get_subtotal(self):
        return sum(item.get_total() for item in self.items)
    
    def get_tax(self, tax_rate=0.08):
        """Calculate tax (default 8%)"""
        return self.get_subtotal() * tax_rate
    
    def get_total(self, tax_rate=0.08):
        return self.get_subtotal() + self.get_tax(tax_rate)
    
    def print_receipt(self, vendor_name="Fresh Produce Stand", tax_rate=0.08):
        """Print formatted cash receipt"""
        print("\n" + "="*50)
        print(f"{vendor_name.center(50)}")
        print("="*50)
        print(f"{'Item':<25} {'Qty/Wgt':<12} {'Total':>10}")
        print("-"*50)
        
        for item in self.items:
            if isinstance(item, ByWeightItem):
                qty_display = f"{item.weight_lb} lb"
            else:
                qty_display = f"{item.quantity} each"
            
            print(f"{item.name:<25} {qty_display:<12} ${item.get_total():>9.2f}")
        
        print("-"*50)
        print(f"{'Subtotal':<37} ${self.get_subtotal():>9.2f}")
        print(f"{'Tax (8%)':<37} ${self.get_tax(tax_rate):>9.2f}")
        print("="*50)
        print(f"{'TOTAL':<37} ${self.get_total(tax_rate):>9.2f}")
        print("="*50)
        print("\nThank you for your purchase!")
        print("="*50 + "\n")


# ============ DRIVER CODE ============

# Create a new order
order = Order()

# Add items to the order
order.add_item(ByWeightItem("Apples", 1.50, 3.5))
order.add_item(ByWeightItem("Bananas", 0.59, 2.2))
order.add_item(ByWeightItem("Tomatoes", 2.99, 1.8))
order.add_item(ByQuantityItem("Lettuce", 2.50, 2))
order.add_item(ByQuantityItem("Avocado", 1.25, 4))

# Print order summary
print("\n" + "="*50)
print("ORDER RECEIPT".center(50))
print("="*50)

# Print all items sorted by cost
items_with_cost = [(item, item.get_total()) for item in order.get_items()]
items_sorted = sorted(items_with_cost, key=lambda x: x[1])

print(f"{'Item':<25} {'Qty/Wgt':<12} {'Cost':>10}")
print("-"*50)

for item, cost in items_sorted:
    if isinstance(item, ByWeightItem):
        qty_display = f"{item.weight_lb} lb"
    else:
        qty_display = f"{item.quantity} each"
    
    print(f"{item.name:<25} {qty_display:<12} ${cost:>9.2f}")

print("-"*50)
print(f"Number of items in order: {len(order)}")
print(f"Total cost of order: ${order.calculate_total():.2f}")
print("="*50 + "\n") 

