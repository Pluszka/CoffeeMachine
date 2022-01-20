from menu import MENU, resources

machineOn=True

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
        if pay(cash):
            resources['water'] -= water
            resources['milk'] -= milk
            resources['coffee'] -= coffee
            return True
        return False

def change(moneyToReturn):
    print(f'Here is ${round(moneyToReturn,2)} dollars in change.')

def onlyGoodCoin():
    validFaceValue=[0.05, 0.01, 0.25, 0.10, 'X'] #TODO add to list X and cancel order
    coin=None
    while not coin in validFaceValue:
        if coin!=None:
            print('Invalid coin.')
        coin=input('Insert coin: $').upper()
        if coin=='X':
            return False
        else:
            coin=float(coin)
    return coin

def insertCoin(bill):
    alreadyIn=0
    print(f'You should pay ${bill}. You can use quarters, dimes, nickles or pennies\n(Press "X" to cancel)')
    while alreadyIn<bill:
        currentCoin=onlyGoodCoin()
        if not currentCoin:
            if alreadyIn>0:
                print(f'Here your money: ${alreadyIn}')
            print('Order canceled.')
            return False
        else:
            alreadyIn+=currentCoin
            print(f'${round(alreadyIn,2)}/${bill}')
    if alreadyIn>bill:
        change(alreadyIn-bill)
    return True

def pay(moneyToPay):
    if insertCoin(moneyToPay):
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


def machine():
    while machineOn:
        whatToDo=onlyGoodOptions()
        makeQuest(whatToDo)

machine()