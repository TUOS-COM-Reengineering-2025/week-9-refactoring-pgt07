class CustomerManager:
    def __init__(self, tax_rate=0.2, tax_threshold=100, discount_threshold=500):
        self.customers = {}
        self.tax_rate = tax_rate#Move Field
        self.tax_threshold = tax_threshold
        self.discount_threshold = discount_threshold

    def add_customer(self, name, purchases):
        if name in self.customers:
            self.customers[name].extend(purchases)
        else:
            self.customers[name] = purchases

    def add_purchase(self, name, purchase):
        self.add_customer(name, [purchase])#Inline Function: reuse add_customer

    def add_purchases(self, name, purchases):
        self.add_customer(name, purchases)#Inline Function

    def calculate_total_with_tax(self, purchases):
        total = 0
        for purchase in purchases:
            total += self.apply_tax(purchase['price'])
        return total

    def apply_tax(self, price):
        # Decompose Condition + Extract Function
        if price > self.tax_threshold:
            return price * (1 + self.tax_rate)
        return price

    def classify_customer(self, total):
        # Decompose condition + Extract Function
        if total > 1000:
            return ["VIP Customer!", "Eligible for discount"]
        elif total > 800:
            return ["Priority Customer", "Eligible for discount"]
        elif total > self.discount_threshold:
            return ["Eligible for discount"]
        elif total > 300:
            return ["Potential future discount customer"]
        else:
            return ["No discount"]

    def generate_report(self):
        for customer_name, purchases in self.customers.items():
            total_spent = self.calculate_total_with_tax(purchases)# Extract Variable
            print(customer_name)
            for status in self.classify_customer(total_spent):# Extract Function
                print(status)

    def calculate_shipping_fee(self, purchases):
        for purchase in purchases:
            if purchase.get('weight', 0) > 20:
                return 50
        return 20

    def contains_heavy_item(self, purchases):
        return any(purchase.get('weight', 0) > 20 for purchase in purchases)# Extract Function

    def contains_fragile_item(self, purchases):
        return any(purchase.get('fragile', False) for purchase in purchases)# Extract Function

def calculate_shipping_fee_for_fragile_items(purchases):
    for purchase in purchases:
        if purchase.get('fragile', False):
            return 60
    return 25


#Remove global functions, already merged as instance methods
