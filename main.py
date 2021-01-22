from data import MENU, resources


def get_coffee_bill(menu_item):
    return MENU[menu_item]


def get_order():
    print("prices")
    print("espresso: $1.50")
    print("latte: $2.50")
    print("cappuccino: $3.00")
    coffee_order = \
        input("What would you like? (espresso/latte/cappuccino): ")\
        .lower()
    return coffee_order


def get_payment():
    print("Please insert coins.")
    quarters = int(input("how many quarters?:"))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = \
        (quarters * .25) \
        + (dimes * .1) \
        + (nickles * .05) \
        + (pennies * .01)
    return total


while True:
    payment_received = False
    your_order = ""
    coffee_received = False
    coffee_command = get_order()

    if coffee_command == 'off':
        total_cost = 0
        quit()
    elif coffee_command == "report":
        total_cost = 0
        print(resources)
    elif coffee_command == "espresso":
        your_order = get_coffee_bill(coffee_command)
        total_cost = your_order["cost"]
    elif coffee_command == "latte":
        your_order = get_coffee_bill(coffee_command)
        total_cost = your_order["cost"]

    elif coffee_command == "cappuccino":
        your_order = get_coffee_bill(coffee_command)
        total_cost = your_order["cost"]
    else:
        total_cost = 0

    missing_ingredients = 0
    machine_water = resources['water']
    coffee_options = ['espresso', "latte", "cappuccino"]
    if coffee_command in coffee_options:
        order_water = your_order['ingredients']['water']
        if coffee_command != "espresso":
            machine_milk = resources['milk']
            order_milk = your_order['ingredients']['milk']
            if machine_milk >= order_milk:
                resources['milk'] -= order_milk
            else:
                print("Sorry there is not enough milk.")
                missing_ingredients += 1

        if machine_water >= order_water:
            resources['water'] -= order_water
        else:
            print("Sorry there is not enough water.")
            missing_ingredients += 1
        machine_coffee = resources['coffee']
        order_coffee = your_order['ingredients']['coffee']
        if machine_coffee >= order_coffee:
            resources['coffee'] -= order_coffee
        else:
            print("Sorry there is not enough coffee.")
            missing_ingredients += 1
        if missing_ingredients == 0:

            if total_cost > 0:
                total_paid = get_payment()

                if total_paid > total_cost and missing_ingredients == 0:
                    change = total_paid - total_cost
                    print(f"Here is ${change} in change.")
                    payment_received = True
                    coffee_received = True
                elif total_paid == total_cost and missing_ingredients == 0:
                    payment_received = True
                    coffee_received = True
                elif total_paid < total_cost and missing_ingredients == 0:
                    print("Sorry that's not enough money. Money refunded.")
                    coffee_received = False
            if coffee_received and missing_ingredients == 0:
                print(f"Here is your {coffee_command} ☕️. Enjoy!")

    response = input("type 'y' to continue")
