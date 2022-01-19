from menu import MENU, resources
import os

machineOn=True

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

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
        if functionality!=None:
            print('Invalid option.')
        functionality = input('What would you like? (espresso(1)/latte(2)/cappuccino(3):')
        clearConsole()
    return functionality
# TODO 2 choose coffe or report
# TODO 3 only correct answers in machine

#machine body
while machineOn:
    whatToDo=onlyGoodOptions()
# TODO 4 cleaning func