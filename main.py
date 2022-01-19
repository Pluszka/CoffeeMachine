from menu import MENU, resources
import os

machineOn=True

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']
    print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney{money}')


def onlyGoodOptions():
    options=['1','2', '3', 'report' ]
    functionality=None
    while functionality not in options:
        if functionality!=None:
            print('Invalid option.')
        functionality = input('What would you like? (espresso(1)/latte(2)/cappuccino(3):')
        clearConsole()
    return functionality


def brew(water, milk, coffee):
    resources['water']-=water
    resources['milk']-=milk
    resources['coffee']-=coffee


def coffe(typeOfCoffe, withmilk):
    product=[typeOfCoffe][0]
    ingredients=product['ingredients']
    price=product['cost']
    if withmilk:
        brew(ingredients['water'],ingredients['milk'],ingredients['coffee'])
    else:
        brew(ingredients['water'],0, ingredients['coffee'])


#TODO espresso diffrent ingredients (no milk)
def makeQuest(quest):
    if quest=='1':
        coffe(MENU['espresso'], False) #TODO 2 def espresso
    elif quest=='2':
        coffe(MENU['latte'], True) #TODO 3 def latte
    elif quest=='3':
        coffe(MENU['cappuccino'], True) #TODO 4 def cappuccino
    else:
        report()


#tests

#machine body
while machineOn:
    whatToDo=onlyGoodOptions()
    makeQuest(whatToDo)
# TODO 1 cleaning func