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
    'bait': 0,
}

for k, v in fishing_inventory.items():
    print("%s,%s" % (k, v))
    time.sleep(1)


# bait hunt functions
def bait_hunt():
    print("Welcome to the woods! It's bait searching time!")
    time.sleep(2)
    print("Searching...")
    time.sleep(1)
    print("Look! %s!" % random.choice(bait_location))
    time.sleep(1)
    print("You've found some %s!" % random.choice(bait_type))
    return fishing_inventory['bait'] + 5



# fishies and baities
fish_type = ["Bass", "Trout", "Carp", "Catfish", "Perch", "Cod", "n Angelfish", "Bluegill"]
bait_type = ["Worms", "Nightcrawlers", "Beetles", "Minnows", "Bread", "Maggots"]
bait_location = ["Under the log", "On the ground", "Next to the tree", "Under that rock", "Next to the mushroom",
                 "In the dirt", "In the puddle"]

def fishing_action():
    if fishing_inventory['bait'] > 2:
        print("You're almost out of bait! Time to go bait hunting!")
        time.sleep(1)
        bait_hunt()

    fishing = input("Would you like to [f]ish,[v]iew stats, or [e]xit?")
    fishing = fishing.strip()
    fishing = fishing.title()

    if fishing == 'F':
        print("Now fishing...")
        time.sleep(2)
        print("...")
        time.sleep(1)
        if random.randrange(0, 100) < 40:
            time.sleep(1)
            print("It's tugging!")
            time.sleep(2)
            print("...")
            time.sleep(1)
            caught_fish = random.choice(fish_type)
            print("You've caught a %s!" % caught_fish)
            fishing_inventory['fish caught'] = fishing_inventory['fish caught'] + [caught_fish]
            fishing_inventory['fish amount'] = fishing_inventory['fish amount'] + 1
            fishing_inventory['bait'] = fishing_inventory['bait'] - 1
        elif random.randrange(0, 100) > 40:
            time.sleep(1)
            print("It's tugging!")
            time.sleep(2)
            print("...")
            time.sleep(1)
            print("The %s got away!" % random.choice(fish_type))
            fishing_inventory['bait'] = fishing_inventory['bait'] - 1
            # rod evolution
            if fishing_inventory['fish amount'] > 2:
                print("Congratulations! Your rod has leveled up to: the Stick Rod!")
                fishing_inventory['current rod'] = 'Nimble Stick Rod'
                print("%s" % fishing_inventory['current rod'])
            if fishing_inventory['fish amount'] > 5:
                print("Congratulations! Your rod has leveled up to: the Pole Rod!")
                fishing_inventory['current rod'] = 'Nimble Pole Rod'
                print("%s" % fishing_inventory['current rod'])
            if fishing_inventory['fish amount'] > 10:
                print("Congratulations! Your rod has leveled up to: the Strong Pole Rod!")
                fishing_inventory['current rod'] = 'Strengthened Pole Rod'
                print("%s" % fishing_inventory['current rod'])
            if fishing_inventory['fish amount'] > 15:
                print("Congratulations! Your rod has leveled up to: the Metal Rod!")
                fishing_inventory['current rod'] = 'Weak Metal Rod'
                print("%s" % fishing_inventory['current rod'])
            if fishing_inventory['fish amount'] > 20:
                print("Congratulations! Your rod has leveled up to: the Strong Metal Rod!")
                fishing_inventory['current rod'] = 'Strengthened Metal Rod'
                print("%s" % fishing_inventory['current rod'])
            elif fishing_inventory['fish amount'] > 30:
                print("Congratulations! Your rod has leveled up to: the Shimano Curado Diamond Rod!")
                fishing_inventory['current rod'] = 'Shimano Curado Diamond Rod'
                print("%s" % fishing_inventory['current rod'])
            else:
                print("")

        if fishing == 'V':
            for key, value in fishing_inventory.items():
                print("%s,%s" % (key, value))
                fishing_action()
        elif fishing == 'E':
            print("Redirecting now...")
            time.sleep(3)
            cont()
        else:
            time.sleep(1)
            fishing_action()
            return end_stats()


play = input("Would you like to [p]lay or [e]xit?")
play = play.strip()
play = play.title()


# end functions
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
    return "Thank you for playing! Here are your final stats: %s" % fishing_inventory


def end_stats():
    print("Thank you for playing! Here are your final stats: ")
    time.sleep(1)

    for key, value in fishing_inventory.items():
        print("%s,%s" % (key, value))
        time.sleep(1)
    return


def restart():
    print("Here are your starting stats: ")
    for k, v in fishing_inventory.items():
        print("%s,%s" % (k, v))
        time.sleep(1)
    return fishing_action()


while play == 'P':
    fishing_action()
    restart()
    bait_hunt()
    cont()
    end_stats()
