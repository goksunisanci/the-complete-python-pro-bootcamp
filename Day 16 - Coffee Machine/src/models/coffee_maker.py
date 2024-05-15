from .menu import Menu
from typing import Dict, List, Union
from .money_machine import MoneyMachine
from ..data.coffee_maker import formatters


class CoffeMaker:
    def __init__(self, menu: Menu, resources: Dict[str, int], money_machine: MoneyMachine):
        self.menu: Menu = menu
        self.resources: Dict[str, int] = resources
        self.money_machine = money_machine

    def check_ingredients(self, drink_name: str) -> Dict[str, Union[bool, List]]:
        drink = self.menu.get_item(drink_name)
        drink_ingredients = drink.get_ingredients()
        information = {"status": True, "missing": []}
        for drink_ingredient, amount in drink_ingredients.items():
            if amount > self.resources.get(drink_ingredient, 0):
                information["status"] = False
                information["missing"].append(drink_ingredient)
        return information

    def make_coffee(self, drink_name: str) -> bool:
        drink = self.menu.get_item(drink_name)
        drink_ingredients = drink.get_ingredients()
        for drink_ingredient, amount in drink_ingredients.items():
            self.resources[drink_ingredient] -= amount
        return True

    def get_report(self) -> Dict[str, str]:
        information = {**self.resources, "money": self.money_machine.money}
        report = {}
        for item, value in information.items():
            information_suffix = formatters[item].get("suffix", "")
            information_prefix = formatters[item].get("prefix", "")
            report[item.capitalize()] = f'{information_prefix}{value}{information_suffix}'
        return report
