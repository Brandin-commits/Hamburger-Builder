import random
#Make a orderable menu


def user_drink():
    drinks = ['water', 'coca-cola', 'sprite', 'lemonade', 'orange juice']
    drink_choice = input(f'And to drink?\nHere are our options: {drinks}')
    if drink_choice in drinks:
        print(f'Good choice on the {drink_choice}.')
    else:
        print('That is not on the menu.')
    


def user_side():
    sides = ['fries', 'mashed potatoes', 'veggies', 'salad', 'soup']
    side_choice = input(f'How about a side? \nThere\'s: {sides} \n')
    if side_choice in sides:
        print(f'Good choice on the {side_choice}.')
    else:
        print('That is not on the menu.')
    


def user_dessert():
    desserts = ['brownie', 'cheese cake', 'carrot cake']
    dessert_choice = input(f'What would you like for dessert?\nOur menu consists of: {desserts} \nWhat would you like?: ')
    if dessert_choice in desserts:
        print(f'Good choice on the {dessert_choice}.')
    else:
        print('That is not on the menu.')


def user_food():
    food = ['cheese burger', 'grilled cheese', 'BLT', 'fried chicken', 'grilled chicken sandwich']
    food_choice = input(f'What entree would you like?\nWe have: {food} \nWhat would you like?: ').strip().lower()
    if food_choice in food:
        print(f'Great you\'ll be having, {food_choice}.')
    else:
        print('Sorry we don\'t have that.')
    


def main():
    print('Hi welcome to the restaurant!')
    user_food()

user_food()
user_drink()
