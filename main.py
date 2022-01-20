from menu import MENU, resources
import os

machineOn=True

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def report():
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']
    print(f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}')


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
        if pay(cash)==True:
            resources['water'] -= water
            resources['milk'] -= milk
            resources['coffee'] -= coffee
            return True
        return False


def onlyGoodCoin():
    validFaceValue=[0.05, 0.01, 0.25, 0.10] #TODO add to list X and cancel order
    coin=None
    while not coin in validFaceValue:
        if coin!=None:
            print('Invalid coin.')
        coin=float(input('Insert coin: $'))
    return coin

def insertCoin(bill):
    alreadyIn=0
    print(f'You should pay ${bill} (Press "X" to cancel)')
    while alreadyIn<bill:
        alreadyIn+=onlyGoodCoin()
        print(f'${alreadyIn}/${bill}')
    return True

def pay(moneyToPay):
    if insertCoin(moneyToPay)==True:
        resources['money'] += moneyToPay
        return True
    return False

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
    if itsOkay==False:
        return None
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
    elif done!=False and done!=None:
        print(f'Sorry there is not enough {done}.')


#tests

#machine body
while machineOn:
    whatToDo=onlyGoodOptions()
    makeQuest(whatToDo)
    clearConsole()
# TODO 1 cleaning func