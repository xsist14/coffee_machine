from data import MENU, resources


def get_coffee_bill(menu_item):
    return MENU[menu_item]["cost"]


def get_order():
    print("prices")
    print("espresso: $1.50")
    print("latte: $2.50")
    print("cappuccino: $3.00")
    coffee_order = \
        input("What would you like? (espresso/latte/cappuccino): ")\
        .lower()
    return coffee_order


def get_payment(num_quarters, num_dimes, num_nickles, num_pennies):
    total = \
              (num_quarters * .25) \
            + (num_dimes * .1) \
            + (num_nickles * .05) \
            + (num_pennies * .01)
    return total


coffee_command = get_order()

if coffee_command == 'report':
    print(resources)
elif coffee_command == 'off':
    quit()
elif coffee_command == "espresso":
    print(MENU["espresso"])
    total_cost = get_coffee_bill(coffee_command)
elif coffee_command == "latte":
    print(MENU["latte"])
    total_cost = get_coffee_bill(coffee_command)
elif coffee_command == "cappuccino":
    print(MENU["cappuccino"])
    total_cost = get_coffee_bill(coffee_command)

# TODO 1: check which coffee was selected
print("Please insert coins.")
quarters = int(input("how many quarters?:"))
dimes = int(input("how many dimes?: "))
nickles = int(input("how many nickles?: "))
pennies = int(input("how many pennies?: "))
total_paid = get_payment(quarters, dimes, nickles, pennies)



# TODO 9: get total cost
# TODO 2: calculate how much money was paid for the coffee
if total_paid > total_cost:
    change = total_paid - total_cost
    print(f"Here is ${change} in change.")
elif total_paid < total_cost:
    print("Sorry that's not enough money. Money refunded.")
    # start over

# TODO 3: check for insufficiencies in payment
# TODO 4: check for insufficiencies in ingredients
# insufficient_water_message = "Sorry there is not enough water."
# insufficient_coffee_message = "Sorry there is not enough coffee."
# insufficient_milk_message = "Sorry there is not enough milk."

# TODO 5: give user back correct change

# give_drink_message = f"Here is your {coffee_choice} ☕️. Enjoy!"

# TODO 6: Turn off the Coffee Machine by entering off to the prompt.
# TODO 7: Print report.
