import random
#Make food items on demand

drinks = ['water', 'coca-cola', 'sprite', 'lemonade', 'orange juice', ]

protein = ['beef', 'grilled chicken', 'crispy chicken']

main_salad = ['iceberg lettuce', 'kale']

cheese = ['american', 'provalone', 'chedder', 'swiss', 'pepper jack', 'shredded', 'no']

bun = ['sesame', 'whole wheat', 'lettuce', 'plain']

condiment = ['ketchup', 'mayo', 'mustard']

topping = ['onion', 'mushroom']

veggies = ['lettuce', 'tomato', 'spinach']

dressings = ['italian', 'ranch', 'no', ]

def burger():
    if user_food == 'burger':
        print('Here\'s a burger with ' + burger_ingre + ' in it.')

def salad():
    if user_food == 'salad':
        print('Here\'s a salad with ' + salad_ingre + ' in it.')

burger_ingre = random.choice(bun), random.choice(protein), random.choice(cheese), random.choice(topping), random.choice(condiment)

salad_ingre = random.choice(main_salad), random.choice(cheese), random.choice(veggies), random.choice(dressings)



user_food = input('What do you want to make?: ').lower().strip()






#Print one of each
print('Here\'s a '+ user_food + ' with a '+  random.choice(protein),', '+ random.choice(cheese),'cheese, '+ random.choice(bun),'bun, '+ random.choice(condiment),'and, '+ random.choice(topping)+'!')
#ChatGPT used to find out how to use 'random.choice' instead of 'random.protein'