from functools import wraps


def currency(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return '$' + str(f(*args, **kwargs))

    return wrapper

class Product:

    def __init__(self, prodDetails):
        self.name = prodDetails['name']
        self.price = prodDetails['price']

    @currency
    def price_with_tax(self, tax_rate_percentage):
        """Return the price with *tax_rate_percentage* applied.
        *tax_rate_percentage* is the tax rate expressed as a float, like "7.0"
        for a 7% tax rate."""
        return round(self.price * (1 + tax_rate_percentage * .01), 2)

print("starting")
prod1Details = {'name': "legos", 'price': 39.99}
prod1 = Product(prod1Details)
print(f"price with tax = {prod1.price_with_tax(7)}")