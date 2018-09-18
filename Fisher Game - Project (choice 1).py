# fisher game

import random
import time


print("Welcome to The Strike! -- a fishing game for all ages.")
time.sleep(1)
name = input("What is your name?")
name = name.title()
name = name.strip()
time.sleep(1)
print("Here are your stats: ")
fishing_inventory = {
    'current rod': "Bamboo",
    'fish caught': [],
    'fish amount': 0,
    'fisherman': name,
    'bait': 5,
    }
for k,v in fishing_inventory.items(): 
    print ("%s,%s" %(k,v))
    time.sleep(1)

    def fishing_action():
        fishing = input("What would you like to do? [f]ish,[v]iew stats, or [e]xit?")
        print ("You chose %s." %fishing)
        if fishing == 'f':
            print("Now fishing...")
            time.sleep(4)
            print("...")
            time.sleep(1)
            if fishing_inventory['bait'] < 2:
                print("You're almost out of bait! Time to go bait hunting!")
                time.sleep(1)
                bait_hunt()
                fishing_action()
            elif fishing_inventory['bait'] > 2:
                print("Bait is on rod!")
        if random.randrange(0,100) < 40:
            print("It's tugging!")
            time.sleep(2)
            print("...")
            time.sleep(1)
            caught_fish = random.choice(fish_type)
            print("You've caught a %s!" %caught_fish)
            fishing_inventory['fish caught'] = fishing_inventory['fish caught'] + [caught_fish]
            fishing_inventory['fish amount'] = fishing_inventory['fish amount'] + 1
            fishing_inventory['bait'] = fishing_inventory['bait'] - 1
        elif random.randrange(0,100) > 40:
            print("It's tugging!")
            time.sleep(2)
            print("...")
            time.sleep(1)
            print("The %s got away!" %random.choice(fish_type))
            fishing_inventory['bait'] = fishing_inventory['bait'] - 1
# rod evolution
        if fishing_inventory['fish caught'] < 2:
            print("Congratulations! Your rod has leveled up to: the Stick Rod!")
            fishing_inventory['current rod'] = 'Nimble Stick Rod'
            print("%s" %fishing_inventory['current rod'])
        if fishing_inventory['fish caught'] < 5:
            print("Congratulations! Your rod has leveled up to: the Pole Rod!")
            fishing_inventory['current rod'] = 'Nimble Pole Rod'
            print("%s"%fishing_inventory['current rod'])
        if fishing_inventory['fish caught'] > 10:
            print("Congratulations! Your rod has leveled up to: the Strong Pole Rod!")
            fishing_inventory['current rod'] = 'Strengthened Pole Rod'
            print("%s" %fishing_inventory['current rod'])
        if fishing_inventory['fish caught'] > 15:
            print("Congratulations! Your rod has leveled up to: the Metal Rod!")
            fishing_inventory['current rod'] = 'Weak Metal Rod'
            print("%s" %fishing_inventory['current rod'])
        if fishing_inventory['fish caught'] > 20:
            print("Congratulations! Your rod has leveled up to: the Strong Metal Rod!")
            fishing_inventory['current rod'] = 'Strengthened Metal Rod'
            print("%s" %fishing_inventory['current rod'])
        elif fishing_inventory['fish caught'] > 30:
            print("Congratulations! Your rod has leveled up to: the Shimano Curado Diamond Rod!")
            fishing_inventory['current rod'] = 'Shimano Curado Diamond Rod'
            print("%s" %fishing_inventory['current rod'])
        else:
            print("")

        if fishing == 'v':
            for k,v in fishing_inventory.items(): 
                print ("%s,%s" %(k,v))
                fishing_action()
        elif fishing == 'e':
            print("Redirecting now...")
            time.sleep(3)
            cont()
        else:
            print("Please enter a valid input.")       
        return ("Here are your new stats: %s" %fishing_inventory)

def restart():
    for k,v in fishing_inventory.items(): 
        print ("Here are your starting stats: %s,%s" %(k,v))
    return fishing_action()
    
# bait hunt function
def bait_hunt():
    print("Welcome to the woods! It's bait searching time!")
    time.sleep(2)
    print("Searching...")
    time.sleep(1)
    print("Look! %s!" %random.choice(bait_location))
    time.sleep(1)
    print("You've found some %s!" %random.choice(bait_type))
    return fishing_inventory['bait'] + 5

fish_type=["Bass","Trout","Carp","Catfish","Perch","Cod","Angelfish","Bluegill"]
bait_type=["Worm","Nightcrawler","Beetle","Minnow","Bread","Maggot"]
bait_location=["Under the log","On the ground","Next to the tree","Under that rock","Next to the mushroom","In the dirt","Inside the puddle"]


play = input("Press [p]lay or [e]xit.")
while play == 'p':

    def cont():
        cont = input("Are you sure? Would you like to [c]ontinue, or [e]xit? You are allowed to [r]estart.")
        if cont == 'c':
            fishing_action()
        if cont == 'e':
            print("Exiting Program...")
            time.sleep(1)
        elif cont == 'r':
            restart()
        else:
            print("Please enter a valid input.")
        return ("Thank you for playing! Here are your final stats: %s" %fishing_inventory)
fishing_action()






    
