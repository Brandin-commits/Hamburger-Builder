import random
#Make a orderable menu


def user_drink():
    drinks = ['water', 'coca-cola', 'sprite', 'lemonade', 'orange juice']
    drink_choice = input(f'And to drink?\nHere are our options: {drinks}\n')
    if drink_choice in drinks:
        print(f'Good choice on the {drink_choice}.')
        return(drink_choice)
    else:
        print('That is not on the menu.')
    

def user_side():
    sides = ['fries', 'mashed potatoes', 'veggies', 'salad', 'soup']
    side_choice = input(f'How about a side? \nThere\'s: {sides}\n')
    if side_choice in sides:
        print(f'Good choice on the {side_choice}.')
        return(side_choice)
    else:
        print('That is not on the menu.')   


def user_dessert():
    desserts = ['brownie', 'cheese cake', 'carrot cake']
    dessert_choice = input(f'What would you like for dessert?\nOur menu consists of: {desserts} \nWhat would you like?: ')
    if dessert_choice in desserts:
        print(f'Good choice on the {dessert_choice}.')
        return(dessert_choice)
    else:
        print('That is not on the menu.')


def user_food():
    food = ['cheese burger', 'grilled cheese', 'blt', 'fried chicken', 'grilled chicken sandwich']
    food_choice = input(f'What entree would you like?\nWe have: {food} \nWhat would you like?: ').strip().lower()
    if food_choice in food:
        print(f'Great you\'ll be having, {food_choice}.')
        return(food_choice)
    else:
        print('Sorry we don\'t have that.')


def user_order():
    print(f'So you be having a drink_choice with food_choice and side_choice. After you\'ll have a dessert_choice.')    
# I can't get 'item'_choice to be grasped within this function

def main():
    print('Hi welcome to the restaurant!')
    user_drink()
    user_food()
    user_side()
    user_dessert()
    user_order()

user_drink()
