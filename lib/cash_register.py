#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, item, price, quantity=1):
        transaction_total = price * quantity
        self.total += transaction_total
        self.items.extend([item] * quantity)
        return {"item": item, "quantity": quantity, "price": price, "total": transaction_total}

    def apply_discount(self):
        if self.discount:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.items:
            return "There are no transactions to void."
        
        last_transaction = self.items[-1]
        last_transaction_total = last_transaction["total"]
        self.total -= last_transaction_total
        self.items.pop()
        return f"Voided transaction for {last_transaction['quantity']} {last_transaction['item']}(s) at ${last_transaction_total}."
