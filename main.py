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
    options=['1','2', '3', 'report','off' ]
    functionality=None
    while functionality not in options:
        if functionality!=None:
            print('Invalid option.')
        functionality = input('What would you like? (espresso(1)/latte(2)/cappuccino(3):')
        clearConsole()
    return functionality


def brew(water, milk, coffee, cash):
    if resources['water']<water:
        return 'water'
    elif resources['milk']<milk:
        return 'milk'
    elif resources['coffee']<coffee:
        return 'coffe'
    else:
        pay(cash)
        resources['water'] -= water
        resources['milk'] -= milk
        resources['coffee'] -= coffee
        return True

def pay(moneyToPay):
    #TODO bring money from consumer
    resources['money'] += moneyToPay
    return True

def coffe(typeOfCoffe, withmilk):
    product=[typeOfCoffe][0]
    ingredients=product['ingredients']
    price=product['cost']  #TODO pay func must return a bolean
    if withmilk:
        itsOkay=brew(ingredients['water'],ingredients['milk'],ingredients['coffee'], price)
    else:
        itsOkay=brew(ingredients['water'],0, ingredients['coffee'], price)
    if itsOkay==True:
        return True
    else:
        return itsOkay


#TODO i must make better corelation with numbers and coffees

def makeQuest(quest):
    global machineOn
    done=False
    listoOfCoffe={'1':'espresso', '2':'latte', '3':'cappuccino'}
    if quest=='1':
        done=coffe(MENU[listoOfCoffe['1']], False)
    elif quest=='2':
        done=coffe(MENU[listoOfCoffe['2']], True)
    elif quest=='3':
        done=coffe(MENU[listoOfCoffe['3']], True)
    elif quest=='off':
        machineOn=False
    else:
        report()
    if done==True:
        print(f'Here is your {listoOfCoffe[quest]}. Enjoy!')
    elif done!=False:
        print(f'Sorry there is not enough {done}.')


#tests

#machine body
while machineOn:
    whatToDo=onlyGoodOptions()
    makeQuest(whatToDo)

# TODO 1 cleaning func