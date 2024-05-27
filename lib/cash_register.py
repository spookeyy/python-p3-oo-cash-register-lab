#!/usr/bin/env python3
# a discount of 20 means the customer receives 20% off their total price.
# Hint 1: to access an attr or call an instance method inside another instance method, use self 
# key word to refer to the instance on which we are operating. for example:
    # example: 
    # class Person:
    #   def __init__(self, age=0):
    #     self.age = age
    #   def birthday(self):
    #     self.age += 1
class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.append((title, price, quantity))

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        elif self.discount > 0:
            self.total = self.total * (1 - self.discount / 100)
            self.print_discount_message()

    def print_discount_message(self):
        discounted_total = self.total
        original_total = self.total / (1 - self.discount / 100)
        discounted_total_rounded = int(round(discounted_total))
        print(f"After the discount, the total comes to ${discounted_total_rounded}.")
    def void_last_transaction(self):
        if len(self.items) > 0:
            last_item = self.items.pop()
            title, price, quantity = last_item
            self.total -= price * quantity
    def items_list(self):
        return [item[0] for item in self.items]

    def items_list_with_quantities(self):
        return [(item[0], item[2]) for item in self.items]

    def items_list_without_multiples(self):
        return [item[0] for item in self.items if item[2] == 1]

    def items_list_with_multiples(self):
        items_with_multiples = []
        for item in self.items:
            title, price, quantity = item
            items_with_multiples.extend([title] * quantity)
        return items_with_multiples
    
    def void_last_transaction_with_multiples(self):
        if len(self.items) > 0:
            self.total -= self.items[-1][1] * self.items[-1][2]

new_register = CashRegister()
new_register.add_item("eggs", 1.99)
new_register.add_item("tomato", 1.76)
print(new_register.items_list())

# register = CashRegister(discount=20)
# register.add_item("Book", 1000, 1)
# register.add_item("Pen", 5)
# register.apply_discount()
# print(register.total)