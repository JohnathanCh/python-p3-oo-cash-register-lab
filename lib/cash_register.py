#!/usr/bin/env python3
import pdb

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.cart = []
    self.items = []
    
  def add_item(self, item_name, price, quantity = 1):
    for num in range(0, quantity):
      item = {item_name: price}
      self.total += price
      self.cart.append(item)
      self.items.append(item_name)
      self.last_item = {item_name: price * quantity}
      
  def apply_discount(self):
    if self.discount > 0:
      self.total -= self.total * (float(self.discount) / 100)
      # pdb.set_trace()
      print(f"After the discount, the total comes to ${int(self.total)}.")
      # return f"After the discount, the total comes to ${int(self.total)}."
    else:
      print("There is no discount to apply.")
      
  def void_last_transaction(self):
    item_name = self.items.pop()
    self.cart.pop()
    self.total -= self.last_item[item_name]
    # pdb.set_trace()
