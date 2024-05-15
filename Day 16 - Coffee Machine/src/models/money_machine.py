from typing import Dict
from .drink import Drink


class MoneyMachine:

    def __init__(self, money: float):
        self.money = money

    def calculate_payment(self, payment_info: Dict[str, int]) -> float:
        inserted_quarters_value = payment_info.get("quarter", 0) * 0.25
        inserted_dimes_value = payment_info.get("dime", 0) * 0.10
        inserted_nickels_value = payment_info.get("nickel", 0) * 0.05
        inserted_pennies_value = payment_info.get("penny", 0) * 0.01
        payment = inserted_quarters_value + inserted_dimes_value + inserted_nickels_value + inserted_pennies_value

        return payment

    def check_payment(self, payment: float, drink: Drink):
        drink_price: float = drink.get_price()

        return payment >= drink_price

    def make_payment(self, payment_info: Dict[str, int], drink: Drink):
        payment = self.calculate_payment(payment_info)
        is_sufficient = self.check_payment(payment, drink)
        info = {"status": False, "remaining": 0}

        if is_sufficient:
            self.money += drink.get_price()
            remaining = round(payment - drink.get_price(), 2)
            info = {"status": True, "remaining": remaining}

        return info
