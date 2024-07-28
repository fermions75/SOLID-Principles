class Order:
    def __init__(self, items, shipping_method):
        self.items = items
        self.shipping_method = shipping_method

class ShippingCalculator:
    def calculate(self, order):
        if order.shipping_method == 'standard':
            return self.calculate_standard(order)
        elif order.shipping_method == 'express':
            return self.calculate_express(order)

    def calculate_standard(self, order):
        return sum(item['price'] for item in order.items) * 0.1

    def calculate_express(self, order):
        return sum(item['price'] for item in order.items) * 0.2

"""
In this example, the ShippingCalculator class needs to be modified whenever a new shipping method is added. This violates the Open/Closed Principle.
We can rewrite the class so that it is open for extension but closed for modification.
"""



class ShippingMethod:
    def calculate(self, order: Order):
        pass


class Order:
    def __init__(self, items, shipping_method: ShippingMethod):
        self.items = items
        self.shipping_method = shipping_method


class StandardShipping(ShippingMethod):
    def calculate(self, order: Order):
        return sum(item['price'] for item in order.items) * 0.1

class ExpressShipping(ShippingMethod):
    def calculate(self, order: Order):
        return sum(item['price'] for item in order.items) * 0.2

class ShippingCalculator:
    def calculate(self, order: Order):
        return order.shipping_method.calculate(order)
    

# Usage
standard_shipping = StandardShipping()
order = Order(items=[{'price': 100}, {'price': 200}], shipping_method=standard_shipping)
calculator = ShippingCalculator()
print(calculator.calculate(order))  # Output: 30.0

express_shipping = ExpressShipping()
order_express = Order(items=[{'price': 100}, {'price': 200}], shipping_method=express_shipping)
print(calculator.calculate(order_express))  # Output: 60.0


"""
The above implementation follows the Open/Closed Principle. The ShippingCalculator class is now open for extension but closed for modification.
Even if a new shipping method is added, the ShippingCalculator class does not need to be modified. We can simply create a new class that extends the ShippingMethod class and implement the calculate method.
"""