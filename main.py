from menu import MENU, resources

# TODO 1 print resorces of machine
def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    print(f'Water: {water}\nMilk: {milk}\nCoffee: {coffee}')

# TODO 2 choose coffe or report
report()