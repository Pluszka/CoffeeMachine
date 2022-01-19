from menu import MENU, resources

# TODO 1 print resorces of machine
def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    print(f'Water: {water}\nMilk: {milk}\nCoffee: {coffee}')

def onlyGoodOptions():
    options=['1','2', '3', 'report' ]
    functionality=None
    while functionality not in options:
        functionality = input('What would you like? (espresso(1)/latte(2)/cappuccino(3):')
    return functionality
# TODO 2 choose coffe or report
# TODO 3 only correct answers in machine

#machine body
whatToDo=onlyGoodOptions()
# TODO 4 