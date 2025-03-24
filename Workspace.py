import random
#Make a orderable menu


def user_drink():
    drinks = ['water', 'coca-cola', 'sprite', 'lemonade', 'orange juice']
    drink_choice = input(f'What would you like to drink?\nHere are our options: {drinks}\n')
    if drink_choice in drinks:
        print(f'Good choice on the {drink_choice}.')
        return drink_choice
    else:
        print('That is not on the menu.')
        return user_drink()
    

def user_side():
    sides = ['fries', 'mashed potatoes', 'veggies', 'salad', 'soup']
    side_choice = input(f'How about a side? \nThere\'s: {sides}\n')
    if side_choice in sides:
        print(f'Good choice on the {side_choice}.')
        return side_choice
    else:
        print('That is not on the menu.')
        return user_side()


def user_dessert():
    desserts = ['brownie', 'cheese cake', 'carrot cake']
    dessert_choice = input(f'What would you like for dessert?\nOur menu consists of: {desserts} \nWhat would you like?: ')
    if dessert_choice in desserts:
        print(f'Good choice on the {dessert_choice}.')
        return dessert_choice
    else:
        print('That is not on the menu.')
        return user_dessert()


def user_food():
    food = ['cheese burger', 'grilled cheese', 'blt', 'fried chicken', 'grilled chicken sandwich']
    food_choice = input(f'What entree would you like?\nWe have: {food} \nWhat would you like?: ').strip().lower()
    if food_choice in food:
        print(f'Great you\'ll be having, {food_choice}.')
        return food_choice
    else:
        print('Sorry we don\'t have that.')
        return user_food()


def user_order(drink, food, side, dessert):
    print(f"\nYour final order:")
    print(f"Drink: {drink}")
    print(f"Entree: {food}")
    print(f"Side: {side}")
    print(f"Dessert: {dessert}")
    print("Thank you for ordering with us!")
   
   # I can't get 'item'_choice to be grasped within this function

def main():
    print('Hi welcome to the restaurant!')
    drink = user_drink()
    food = user_food()
    side = user_side()
    dessert = user_dessert()
    user_order(drink, food, side, dessert)

main()
