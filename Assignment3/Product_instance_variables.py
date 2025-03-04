class Product:
    discount_rate = 10  # Class variable
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def discounted_price(self):
        return self.price - (self.price * Product.discount_rate / 100)

# Example usage
product = Product("Laptop", 50000)
print(product.discounted_price())  # Output: 45000.0