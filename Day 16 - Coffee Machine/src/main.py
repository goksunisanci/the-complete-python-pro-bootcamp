from src.models.coffee_maker import CoffeMaker
from src.models.drink import Drink
from src.models.menu import Menu
from src.models.money_machine import MoneyMachine
from src.data.coffee_maker import resources
from src.data.menu import MENU

money_machine = MoneyMachine(0)
drinks = {}

for product_name, product_info in MENU.items():
    price = product_info["cost"]
    ingredients = {}
    for ingredient, amount in product_info["ingredients"].items():
        ingredients[ingredient] = amount

    drinks[product_name] = Drink(ingredients, price)

menu = Menu(drinks)
coffee_maker = CoffeMaker(menu, resources, money_machine)

while True:

    customer_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if customer_choice == "off":
        break
    elif customer_choice == "report":
        report = coffee_maker.get_report()
        print(report)
        continue
    elif customer_choice not in ["espresso", "latte", "cappuccino"]:
        print("Choose from the menu!")
        continue

    sufficient_ingredients_information = coffee_maker.check_ingredients(customer_choice)
    if not sufficient_ingredients_information["status"]:
        missing_ingredients = sufficient_ingredients_information["missing"]
        print(f'Sorry. There is not enough {", ".join(missing_ingredients)}.')
        continue

    print("Time to make payment.")
    payment_quarter = int(input("How many quarter you will insert?"))
    payment_dime = int(input("How many dime you will insert?"))
    payment_nickel = int(input("How many nickel you will insert?"))
    payment_penny = int(input("How many penny you will insert?"))

    payment_info = {"quarter": payment_quarter,
                    "dime": payment_dime,
                    "nickel": payment_nickel,
                    "penny": payment_penny
                    }
    sufficient_money_information = money_machine.make_payment(payment_info, menu.get_item(customer_choice))
    if not sufficient_money_information["status"]:
        print("Sorry. That's not enough money. Money refunded.")
        continue

    remaining_money = sufficient_money_information["remaining"]
    if remaining_money > 0:
        print(f'Here is ${remaining_money} dollars in change.')

    make_coffee = coffee_maker.make_coffee(customer_choice)
    print(f'Here is your {customer_choice} ☕. Enjoy!')
