# omar de la osa, fisher game
# 9/24/18

import random
import time

print("Welcome to The Strike! -- a fishing game for all ages.")
time.sleep(1)
name = input("What is your name?")
name = name.title()
name = name.strip()
time.sleep(1)
print("Here are your stats: ")
time.sleep(1)
fishing_inventory = {
    'current rod': "Bamboo",
    'fish caught': [],
    'fish amount': 0,
    'fisherman': name,
    'bait': 5,
}

for k, v in fishing_inventory.items():
    print("%s,%s" % (k, v))
    time.sleep(1)


# bait hunt function
def bait_hunt():
    time.sleep(1)
    print("*Pokemon Red Theme plays*")
    time.sleep(0.5)
    print("Welcome to the woods! It's bait searching time!")
    time.sleep(2)
    print("Searching...")
    time.sleep(1)
    print("Look! %s!" % random.choice(bait_location))
    time.sleep(1)
    print("You've found some %s!" % random.choice(bait_type))
    time.sleep(2)
    print("Bait is restored!")
    time.sleep(1)
    print("Returning to fishing spot...")
    time.sleep(1)
    fishing_inventory['bait'] += 5
    return fishing_action()

# fishies and baities
fish_type = ["Bass", "Trout", "Carp", "Catfish", "Perch", "Cod", "Angelfish", "Bluegill","Sunfish","Rainbow Trout","Walleye"]
bait_type = ["Worms", "Nightcrawlers", "Beetles", "Minnows", "Bread", "Maggots"]
bait_location = ["Under the log", "On the ground", "Next to the tree", "Under that rock", "Next to the mushroom",
                 "In the dirt", "In the puddle"]

def fishing_action():
    if fishing_inventory['bait'] == 2:
        print("You're almost out of bait! Time to go bait hunting!")
        time.sleep(1)
        return bait_hunt()
    else:
        print("")

    fishing = input("Would you like to [f]ish,[v]iew stats, or [e]xit?")
    fishing = fishing.title()
    fishing = fishing.strip()

    if fishing == 'F':
        print("Now fishing...")
        time.sleep(2)
        print("...")
        time.sleep(1)

        if random.randrange(0,100) < 40:
            time.sleep(1)
            print("It's tugging!")
            time.sleep(2)
            print("...")
            time.sleep(1)
            caught_fish = random.choice(fish_type)
            fishing_inventory['fish caught'] = fishing_inventory['fish caught'] + [caught_fish]
            fishing_inventory['fish amount'] = fishing_inventory['fish amount'] + 1
            fishing_inventory['bait'] = fishing_inventory['bait'] - 1
            print("You've caught a %s!" % caught_fish)
        elif random.randrange(0,100) > 40:
            time.sleep(1)
            print("It's tugging!")
            time.sleep(2)
            print("...")
            time.sleep(1)
            fishing_inventory['bait'] = fishing_inventory['bait'] - 1
            print("The %s got away!" % random.choice(fish_type))
        else:
            time.sleep(2)
            fishing_inventory['bait'] = fishing_inventory['bait'] - 1
            print("Not even a bite!")

            print("")
    if fishing == 'V':
        print("Here are your stats: ")
        for k, v in fishing_inventory.items():
            print("%s,%s" % (k, v))
            time.sleep(1)
        return fishing_action()
    elif fishing == 'E':
        print("Redirecting now...")
        time.sleep(3)
        return cont()
    else:
        time.sleep(1)
        return fishing_action()


play = input("Would you like to [p]lay or [e]xit?")
play = play.strip()
play = play.title()


# end functions
def cont():
    cont = input("Are you sure? Would you like to [c]ontinue, or [e]xit?")
    cont = cont.lower()
    cont = cont.strip()
    if cont == 'e':
        print("Exiting Program...")
        time.sleep(1)
        print("Thank you for playing! Here are your final stats: %s" % fishing_inventory)
        print("Program Closing...")
        return breakpoint()
    elif cont == 'c':
        return fishing_action()
    else:
        print("")


def end_stats():
    print("Thank you for playing! Here are your final stats: ")
    time.sleep(1)

    for key, value in fishing_inventory.items():
        print("%s,%s" % (key, value))
        time.sleep(1)
    return ""




while play == 'P':
    fishing_action()
    bait_hunt()
    cont()
    end_stats()
