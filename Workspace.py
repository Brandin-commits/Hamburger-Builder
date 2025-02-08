import random
#Make a orderable menu

drinks = ['water', 'coca-cola', 'sprite', 'lemonade', 'orange juice']

sides = ['fries', 'mashed potatoes', 'veggies', 'salad', 'soup']

dessert = ['brownie', 'cheese cake', 'carrot cake']

food = ['cheese burger', 'grilled cheese', 'BLT', 'fried chicken', 'grilled chicken sandwich']


def user_order():
    print(user_food, user_side, user_drink, user_dessert)


def user_drink():
    print('Here are our drink options: ')


def user_side():
    print('How about a side? \nThere\'s:' + sides + '\n')


def user_dessert():
    print('What would you like for dessert?\nOur menu consists of: ' + dessert + '\nWhat would you like?: ')


def user_food():
    print('What entree would you like?\nWe have: ' + food + '\nWhat would you like?: ')


def burger():
    if user_food == 'burger':
        print(f'Here\'s a burger with ' + burger_ingre + ' in it.')


def salad():
    if user_food == 'salad':
        print(f'Here\'s a salad with ' + salad_ingre + ' in it.')


def main():
    
    if user_food == 'burger':
        burger()
    elif user_food == 'salad':
        salad()
    else:
        print('Option not available. ')


main()