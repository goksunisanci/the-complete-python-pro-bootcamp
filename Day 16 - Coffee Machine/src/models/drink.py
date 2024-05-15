from typing import Dict


class Drink:
    def __init__(self, ingredients: Dict[str, int], price: float):
        self.ingredients: Dict[str, int] = ingredients
        self.price: float = price

    def get_ingredients(self) -> Dict[str, int]:
        return self.ingredients

    def get_price(self) -> float:
        return self.price
