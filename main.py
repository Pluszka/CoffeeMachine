from menu import MENU, resources

# TODO 1 print resorces of machine
def report(currentCondition):
    water = currentCondition['water']
    milk = currentCondition['milk']
    coffee = currentCondition['coffee']
    print(f'Water: {water}\nMilk: {milk}\nCoffee: {coffee}')


report(resources)