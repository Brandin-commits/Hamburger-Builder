import random

def getTyoeOfCheese():
    cheese = ['swiss', 'chedder', 'provalone']
    return random.choice(cheese)
#Make hamburger with random ingredients each time
protein = ['beef']

cheese = ['american', 'provalone', 'chedder', 'swiss', 'pepper jack']

bun = ['sesame', 'whole wheat', 'lettuce', 'plain']

condiment = ['ketchup', 'mayo', 'mustard']

topping = ['onion', 'lettuce', 'tomato', 'mushroom']

#Print one of each
print('Here\'s a hamburger with a '+  random.choice(protein),'patty, '+ getTyoeOfCheese(),'cheese, '+ random.choice(bun),'bun, '+ random.choice(condiment),'and, '+ random.choice(topping)+'!')
#ChatGPT used to find out how to use 'random.choice' instead of 'random.protein'