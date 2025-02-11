import random
#Make a orderable menu



def user_order():
    
    
    print(f'Here\'s your order: {order})


def user_drink():
    drinks = ['water', 'coca-cola', 'sprite', 'lemonade', 'orange juice']
    print(f'Here are our drink options: {drinks}')


def user_side():
    sides = ['fries', 'mashed potatoes', 'veggies', 'salad', 'soup']
    print(f'How about a side? \nThere\'s:{sides} \n')


def user_dessert():
    desserts = ['brownie', 'cheese cake', 'carrot cake']
    print(f'What would you like for dessert?\nOur menu consists of: {desserts} \nWhat would you like?: ')


def user_food():
    food = ['cheese burger', 'grilled cheese', 'BLT', 'fried chicken', 'grilled chicken sandwich']
    print(f'What entree would you like?\nWe have:  {food} \nWhat would you like?: ')
    

def burger():
    if user_food == 'burger':
        print(f'Here\'s a burger with {burger} in it.')


def salad():
    if user_food == 'salad':
        print(f'Here\'s a salad with {salad} in it.')


def main():
    user_food()


main()