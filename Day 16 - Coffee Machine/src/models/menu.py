from typing import Dict
from .drink import Drink


class Menu:
    def __init__(self, items_list: Dict[str, Drink]):
        self.menu: Dict[str, Drink] = items_list

    def get_item(self, item_name: str) -> Drink:
        if item_name in self.menu:
            return self.menu[item_name]
