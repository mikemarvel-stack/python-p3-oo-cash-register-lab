#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self._last_transaction = 0

  def add_item(self, title, price, quantity=1):
        increment = price * quantity
        self.total += increment
        self._last_transaction = increment    
        self.items.extend([title] * quantity)

  def apply_discount(self):
        if self.discount:
            self.total = int(self.total * (100 - self.discount) / 100)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

  def void_last_transaction(self):
        self.total -= self._last_transaction        
        self.total = round(self.total, 2)
        if self.total < 0:
            self.total = 0.0

  pass
