import random
import time 
import sys
from time import sleep


got_planks = False
got_parachute = False
got_honeycomb = False
got_axe = False
got_cutlass = False
your_health = 75
given_clue = False
got_hammer_and_nails = False
got_rum_bottle = False
pirates_health = 75
squirrel_health = 60

times_in_mush_forest = 0


# ---------------- Credits ---------------------


def print_slow(str):
    for char in str:
            time.sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()

def credits():
    print_slow("ＦＩＮ．")
    print("\n\n\n")
    print_slow("""You've got a friend in me
You've got a friend in me
When the road looks rough ahead
And you're miles and miles from your nice warm bed
You just remember what your old pal said
Son you've got a friend in me
Yeah you've got a friend in me
​
You've got a friend in me
You've got a friend in me
You got troubles and I got 'em too
There isn't anything I wouldn't do for you
We stick together, we can see it through
'Cause you've got a friend in me
You've got a friend in me
​
Some other folks might be a little bit smarter than I am
Bigger and stronger too
Maybe
But none of them
Will ever love you the way I do
It's me and you baby
​
And as the years go by
Our friendship will never die
You're gonna see it's our destiny
You've got a friend in me
You just remember what your old pal said
Son you've got a friend in me
We stick together, we can see it through
'Cause you've got a friend in me
Some other folks might be a little bit smarter than I am
Bigger and stronger too
Maybe
But none of them
Will ever love you the way I do
It's me and you baby
And as the years go by
Our friendship will never die
You're gonna see it's our destiny
You've got a friend in me
Yes, you do
You've got a friend in me
Yes you do
You've got a friend in me
Yeah""")
    time.sleep(0.5)
    print("You've Got a Friend in Me: Randy Newman")
    print("\n\n")
    print_slow("Dan Green:\n")
    print("-North Forest")
    time.sleep(1)
    print("-Bear Cave")
    time.sleep(1)
    print("-North Forest")
    time.sleep(1)
    print("-Mushroom Forest")
    time.sleep(1)
    print("-Shipwreck")
    time.sleep(1)
    print("-East Beach")
    time.sleep(1)
    print("\n\n")
    print_slow("Nasra Jeylani:\n")
    print("-Old Hut")
    time.sleep(1)
    print("-Special Effects")
    time.sleep(1)
    print("-Sound")
    time.sleep(1)
    print("\n\n")
    print_slow("Ea-Nkoy Ilondo:\n")
    print("-Bridge")
    time.sleep(1)
    print("-Hair and Make up")
    time.sleep(1)
    print("-Story")
    time.sleep(1)
    print("\n\n")
    print_slow("Kamil:\n")
    print("-Beehive Area")
    time.sleep(1)
    print("-Costume Design")
    time.sleep(1)
    print("-Catering")
    time.sleep(1)
    print("\n\n")
    print_slow("Reyanud Din:\n")
    print("-Dense Jungle")
    time.sleep(1)
    print("-Lake")
    time.sleep(1)
    print("-Lighting")
    time.sleep(1)
    print("\n\n")
    print_slow("Lucas Priestley:\n")
    print("-Pre Game")
    time.sleep(1)
    print("-Old Campsite")
    time.sleep(1)
    print("-Squirrel")
    time.sleep(1)
    print("-End Credits")
    time.sleep(1.5)
    print("\n\n\n")
    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠉⠉⠀⠀⠀⠈⠑⢢⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⢀
⠀⠀⠀⣀⣠⠤⠤⠤⠤⠤⣶⣉⣹⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⣰⠚
⣠⣞⣋⠁⣤⣴⣷⣶⢤⠀⠸⢫⠃⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣆⠀⠀⠀⠀⠀⠀⠀⡟⠉⠀⠀
⡏⠁⠈⠱⡙⢿⣿⣽⣗⠇⠀⠸⠟⢻⣀⣀⣀⠀⠀⠀⠀⠀⠀⢀⡀⠤⠤⠤⠤⠤⠤⢀⣀⠀⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀
⠹⣦⣀⡤⢣⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠒⠒⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⣄⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⢷⠀⠀
⠀⠈⠓⢄⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⢸⠀⠀⠀⠀⠀⠀⠸⠀⠀
⠀⠀⠀⠀⠑⠢⢍⡒⠀⠠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⢣⣀⡼⠀⠀⠀⠀⠀⠀⠈⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠒⠊⠉⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢢⡀⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⢤⣸⠀⠀⠀⠀⠀⣆⠀⠀⢀⣀⠴⠚⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠙⢧⠀⠀⠀⠀⣏⠉⠉⠁⢀⣀⣀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠛⠒⠤⠤⠔⠊⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⠀⣸⠀⠀⠀⢰⠏⠉⠉⠉⠉⠳⣄⠈⠣⣀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⡤⠎⠀⢀⣤⡞⠁⠀⢀⡴⠁⠀⠀⠀⠀⢀⣤⣤⡭⣶⠞⠛⣲⡶⠖⠒⠚⠉⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠾⠿⠿⢤⣴⡶⠛⠉⠀⣠⠔⠉⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⣽⣛⣋⡀⠠⠤⠄⠒⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
    time.sleep(1.5)
    print("\n")
    print("""
████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗██╗░░░██╗░█████╗░██╗░░░██╗  ███████╗░█████╗░██████╗░
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝╚██╗░██╔╝██╔══██╗██║░░░██║  ██╔════╝██╔══██╗██╔══██╗
░░░██║░░░███████║███████║██╔██╗██║█████═╝░░╚████╔╝░██║░░██║██║░░░██║  █████╗░░██║░░██║██████╔╝
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░░░╚██╔╝░░██║░░██║██║░░░██║  ██╔══╝░░██║░░██║██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗░░░██║░░░╚█████╔╝╚██████╔╝  ██║░░░░░╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝
​
██████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗███╗░░██╗░██████╗░░░░
██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██║████╗░██║██╔════╝░░░░
██████╔╝██║░░░░░███████║░╚████╔╝░██║██╔██╗██║██║░░██╗░░░░
██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██║██║╚████║██║░░╚██╗░░░
██║░░░░░███████╗██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝██╗
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝""")
    print("\n")


# -------------------Ending--------------------------

def ending():

    print("You and the Squirrel both hope in the boat")
    print("")
    time.sleep(2.5)
    print("You you set sail for your new life together")
    print("")
    time.sleep(2.5)
    credits()


# ------------------- secret area ----------------

def Secret_Area():
    print()
    time.sleep(1.5)
    print("You made it off the bridge, safely.")
    print()
    time.sleep(1.5)
    print("But the bridge, broke down after you crossed it.")
    print()
    time.sleep(1.5)
    print("You walk a couple of steps, and see a huge ancient structure.")
    print()
    time.sleep(1.5)
    print("You feel like you shouldn't enter.")
    time.sleep(1.5)
    print()
    print("Squirrel: Ahh geez man, that looks scary.")
    print()
    time.sleep(1.5)
    print("Squirrel: But i think you will find something useful in there.")
    print()
    time.sleep(1.5)
    print()
    
    print("You take the squirrels advice and proceed to enter the structure.")
    print()
    time.sleep(1.5)
    print("You enter, and you see a huge hall.")
    print()
    time.sleep(1.5)
    print("In the middle of the hall, theres a podium with something on it.")
    print()
    time.sleep(2)
    print()
    print("Squirrel: Why you looking at me for, go on grab it its your way home.")
    print()
    time.sleep(2.5)
    print("Squirrel: Its what you have been wanting since the begining.")
    print()
    time.sleep(2.5)
    print("Squirrel: Its a portal key, when you pick it off the podium it will open a portal for you.")
    print()
    time.sleep(2.5)
    print("Squirrel: Alright, for god sake stop crying.")
    print()
    time.sleep(1.5)
    print()
    print("You look at the squirrel and see tears in his eyes")
    time.sleep(2)
    print()
    print("Squirrel: Im not pathetic like you, why would i be crying.")
    print()
    time.sleep(2)
    print("Squirrel: Its allergy season alright, something is in my eye.")
    time.sleep(2)
    print()
    print("You proceed to the podium, looking back one more time.")
    print()
    time.sleep(2)
    print("You pick up the key, and a bright light shines in front of you.")
    print()
    time.sleep(2)
    print("It creates a circular entrance, a few steps in front of you.")
    print()
    time.sleep(2)
    print("You enter the portal, the portals light shining on you face.")
    print()
    time.sleep(2)
    print("It feels war and comforting, it reminds you of your home.")
    print()
    time.sleep(2)
    print()
    print()
    time.sleep(1.5)
    print("loading...")
    time.sleep(3)
    print()
    print()
    print("You open your eyes and your in your house, in your room")
    print()
    time.sleep(2)
    print("You feel like it was all a dream, but you look into your hand and you see the portal key.")
    print()
    time.sleep(2.5)
    print("You say out load \"im gunna miss that damn squirrel\".")
    time.sleep(2)
    print()
    print("Squirrel: I gunna miss you too.")
    time.sleep(2)
    print()
    print("You turn around, and you see him just waving at you")
    print()
    time.sleep(3)

    print("END.....")

    credits()


# ----------------Campsite return--------------

def navigation_camp():
    print_slow("Which way would you like to go?")
    print("\n")
    direction = input("North or West: ")
    if direction.lower() == "north" or direction.lower() == "n":
        print_slow("You have decided to take the path that goes North")
        print("\n")
        print_slow("loading...'Dense Jungle'")
        print("\n")
        jungle()

    elif direction.lower() == "east" or direction.lower() == "e":
        print_slow("Squirrel - That's my house! NO ONE..is allowed to go there...")
        print("\n")    
        navigation_camp()

    elif direction.lower() == "south" or direction.lower() == "s":
        print_slow("Squirrel - That will take you back to the Ocean.")
        print("\n")
        print_slow("Squirrel - You don't need to go that way.")
        print("\n")   
        navigation_camp()

    elif direction.lower() == "west" or direction.lower() == "w":
        print_slow("You have decided to go West")
        print("\n")
        print_slow("loading...'Old Hut'")
        print("\n")
        old_Hut() 

    else:
        print_slow("What?")
        print("\n")
        navigation_camp()


def campsite_return():
    print("\n")
    print("\n")
    print("Ｏｌｄ Ｃａｍｐｓｉｔｅ")
    time.sleep(1.5)
    print("\n")
    print_slow("Your back at the old campsite, its nice and safe, but theres nothing to be done here now")
    time.sleep(1.5)
    print("\n")
    print_slow("Squirrel - From here, you can go 'North' to the 'Dense Jungle'...\n\nSquirrel Or 'West' to the 'Old Hut' ")
    navigation_camp()


# ---------------------------- Bee Hive --------------------------


def bee_hive_area():
    print("You have arrived to the Bee Hive Area, You can collect the Honey Comb in here.")
    print()
    time.sleep(2.5)
    print("The Honey Comb distract the Bear at the Bear Cave, so you rush in an loot the cave")
    print()
    time.sleep(2.5)
    print("But, be careful as the swarm of bees may HARM YOU, if you won't play it smart you will die.")
    print()
    time.sleep(2.5) 
    print("If you only knew how to distract the bees...")
    print()
    time.sleep(2.5)


    
    wood_tinder = input("Do you have what it takes to distract bees?")
    if (wood_tinder.lower() == "yes" or wood_tinder.lower() == "y") and got_rum_bottle == True:
        time.sleep(2.5)
        print("You pour the rum onto some wood and create a spark with some rocks")
        print()
        time.sleep(2.5)
        print("You set up the fire under the Bee Hive and the Smoke distracted the Bees while you collected the Honey Comb")
        print()
        global got_honeycomb
        got_honeycomb = True
        print("Now you have the honeycomb you head back south to the mushroom forest")
        print()
        time.sleep(2.5)
        print("Loading... Mushroom forest.")
        print()
        time.sleep(2.5)
        mushroom_forest()
    else:
        if wood_tinder.lower() == "no" or wood_tinder.lower() == "n" or got_rum_bottle == False:
            time.sleep(2.5)
            print("You don't have what it takes to set up the fire")
            print("")
            time.sleep(2.5)
            print("Have you not found any flammable materials?")
            print("")
            solution_1 = input("What potentialy could distract the bees that is given off by fire?")
            if solution_1.lower() == "smoke":
             time.sleep(2.5)
             print("Correct, smoke would distract the bees so you could safely gather the Honey Comb")
             print("")
             time.sleep(2.5)
             print("You should prepare yourself to set up the fire under the Bee Hive.")
             print("")
             time.sleep(2.5)
             print("You would need to find some flammable materials to start the fire")
             print("")
             time.sleep(2.5)
             print("You head back south to search for what you need")
             print("")
             mushroom_forest()
            else:
             time.sleep(2.5)
             print("*You've just realized that smoke would distract the bees*")
             print("")
             time.sleep(2.5)
             print("You should prepare yourself to set up the fire under the Bee Hive.")
             print("")
             time.sleep(2.5)
             print("You would need to find flammable materials to start the fire")
             print("")
             time.sleep(2.5)
             print("You head back south to search for what you need")
             print("")
             mushroom_forest()
        else:
             time.sleep(2.5)
             print("*You've just realized that smoke would distract the bees*")
             print("")
             time.sleep(2.5)
             print("You should prepare yourself to set up the fire under the Bee Hive.")
             print("")
             time.sleep(2.5)
             print("You would need to find flammable materials to start the fire")
             print("")
             time.sleep(2.5)
             print("You head back south to search for what you need")
             print("")
             mushroom_forest()

#------------------------ East Beach ----------------------------------


def east_beach():
    print("As you wander down the path the trees become sparser and it opens up into a little cove.")
    print("")
    time.sleep(2.5)
    print("There are lots of sharp rocks protruding from the water, also on the beach there is a large object...")
    print("")
    time.sleep(2.5)
    print("You run forward excitedly, you think you know what the object is.")
    print("")
    time.sleep(2.5)
    print("Your right!")
    print("")
    time.sleep(1.5)
    print("It's a rowboat!")
    print("")
    time.sleep(1.5)
    print("It has seen better days though, there is a large hole in the side where it must have hit the rocks.")
    print("")
    time.sleep(2.5)
    print("You could probably repair it though if you had the right tools.")
    print("")
    time.sleep(2.5)
    print("Lets see, you would need a hammer & nails, some wood chopped into planks, and a sail, to make it seaworthy.")
    print("")
    time.sleep(2.5)
    if got_hammer_and_nails == True and got_parachute == True and got_planks == True:
        print("Brilliant, you have everything you need.")
        print("")
        time.sleep(2.5)
        print("You begin to work on repairing the boat.")
        print("")
        time.sleep(2.5)
        print("First you patch up the large hole by attatching wooden planks over it with the hammer and nails.")
        print("")
        time.sleep(3)
        print("Then you use the parachute you found to rig up a sail so that it can handle the open seas.")
        print("")
        time.sleep(2.5)
        print("With the boat fully repaired you make ready to set sail.")
        print("")
        time.sleep(2.5)
        ending()

    elif got_hammer_and_nails == True and got_parachute == False and got_planks == True:
        print("Well, you have some of what you need.")
        print("")
        time.sleep(2.5)
        print("You begin to work on repairing the boat.")
        print("")
        time.sleep(2.5)
        print("First you patch up the large hole by attatching wooden planks over it with the hammer and nails.")
        print("")
        time.sleep(3)
        print("But it will still a sail in order to make it seaworthy.")
        print("")
        time.sleep(2.5)
        print("Maybe you can find something on the island that would work.")
        print("")
        time.sleep(2.5)
        print('"As if something like that would just drop from the sky" says your talkative squirrel friend.')
        print("")
        time.sleep(2.5)
        print('"Then again maybe it already has; to the north" suggests the squirrel.')
        print("")
        time.sleep(2.5)
        print("You take the squirrel's advice and head north again back towards the forest lake you found")
        print("")
        time.sleep(2.5)
        Lake()

    elif got_hammer_and_nails == True and got_parachute == False and got_planks == False:
        print("Well, you have some of what you need.")
        print("")
        time.sleep(2.5)
        print("But not enough to begin work on repairing the boat.")
        print("")
        time.sleep(2.5)
        print("You need some wooden planks in order to cover that hole up")
        print("")
        time.sleep(3)
        if got_axe == True:
            print("You could probably use the axe you have to chop up some forest trees into planks")
            print("")
            time.sleep(3)
        elif got_axe == False:
            print("You could really use an axe to chop up some forest trees into planks")
            print("")
            time.sleep(3)       
            print('"Yes an axe certainly is a BEAR necessity the days". Quips the squirrel')
            print("")
            time.sleep(3)  
        print("Even then the boat will still a sail in order to make it seaworthy.")
        print("")
        time.sleep(2.5)
        print("Maybe you can find something on the island that would work.")
        print("")
        time.sleep(2.5)
        print('"As if something like that would just drop from the sky" says your talkative squirrel friend.')
        print("")
        time.sleep(2.5)
        print('"Then again maybe it already has; to the north" suggests the squirrel.')
        print("")
        time.sleep(2.5)
        print("You take the squirrel's advice and head north again back towards the forest lake you found")
        print("")
        time.sleep(2.5)
        Lake()

    elif got_hammer_and_nails == True and got_parachute == True and got_planks == False:
        print("Well, you have some of what you need.")
        print("")
        time.sleep(2.5)
        print("You begin to work on repairing the boat.")
        print("")
        time.sleep(2.5)
        print("You use the parachute you found to rig up a sail so that it can handle the open seas.")
        print("")
        time.sleep(2.5)
        print("You still need some wooden planks in order to cover that hole up")
        print("")
        time.sleep(3)
        if got_axe == True:
            print("You could probably use the axe you have to chop up some forest trees into planks")
            print("")
            time.sleep(3)
        elif got_axe == False:
            print("You could really use an axe to chop up some forest trees into planks")
            print("")
            time.sleep(3)       
            print('"Yes an axe certainly is a BEAR necessity the days". Quips the squirrel')
            print("")
            time.sleep(3)  
        
        print("You will have to head back north to the forest lake in order make some wooden planks")
        print("")
        time.sleep(2.5)
        Lake()  

    elif got_hammer_and_nails == False and got_parachute == True and got_planks == True:
        print("Well, you have some of what you need.")
        print("")
        time.sleep(2.5)
        print("You begin to work on repairing the boat.")
        print("")
        time.sleep(2.5)
        print("You use the parachute you found to rig up a sail so that it can handle the open seas.")
        print("")
        time.sleep(2.5)
        print("You still need a hammer & nails to secure the planks in order to cover that hole up though")
        print("")
        time.sleep(3)
        print("Maybe you can find some on the island.")
        print("")
        time.sleep(2.5)
        print('"Don\'t tell me you didn\'t find your shipreck yet?" says your talkative squirrel friend.')
        print("")
        time.sleep(2.5)
        print('"Thats goin to take so much backtracking all the way to the southern beaches" the squirrel moans.')
        print("")
        time.sleep(2.5)
        print("Unfortunatly you must heed the the squirrel's advice and you backtrack towards the forest lake you found")
        print("")
        time.sleep(2.5)
        Lake()

    elif got_hammer_and_nails == False and got_parachute == True and got_planks == False:
        print("Well, you have some of what you need.")
        print("")
        time.sleep(2.5)
        print("You begin to work on repairing the boat.")
        print("")
        time.sleep(2.5)
        print("You use the parachute you found to rig up a sail so that it can handle the open seas.")
        print("")
        time.sleep(2.5)
        print("You still need a hammer & nails and some planks in order to cover that hole up though")
        print("")
        time.sleep(3)
        if got_axe == True:
            print("You could probably use the axe you have to chop up some forest trees into planks")
            print("")
            time.sleep(3)
        elif got_axe == False:
            print("You could really use an axe to chop up some forest trees into planks")
            print("")
            time.sleep(3)       
            print('"Yes an axe certainly is a BEAR necessity the days". Quips the squirrel')
            print("")
            time.sleep(3)  
        print("As for the hammer and nails; maybe you can find some on the island.")
        print("")
        time.sleep(2.5)
        print('"Don\'t tell me you didn\'t find your shipreck yet?" says your talkative squirrel friend.')
        print("")
        time.sleep(2.5)
        print('"Thats goin to take so much backtracking all the way to the southern beaches" the squirrel moans.')
        print("")
        time.sleep(2.5)
        print("Unfortunatly you must heed the the squirrel's advice and you backtrack towards the forest lake you found")
        print("")
        time.sleep(2.5)
        Lake()

    elif got_hammer_and_nails == False and got_parachute == False and got_planks == True:
        print("Well, you have some of what you need.")
        print("")
        time.sleep(2.5)
        print("But not enough to begin work on repairing the boat.")
        print("")
        time.sleep(2.5)
        print("You still need a hammer & nails to secure the planks in order to cover that hole up")
        print("")
        time.sleep(3)
        print("Maybe you can find some on the island.")
        print("")
        time.sleep(2.5)
        print('"Don\'t tell me you didn\'t find your shipreck yet?" says your talkative squirrel friend.')
        print("")
        time.sleep(2.5)
        print('"Thats goin to take so much backtracking all the way to the southern beaches" the squirrel moans.')
        print("")
        time.sleep(2.5)
        print("And the boat still needs a sail in order to make it seaworthy.")
        print("")
        time.sleep(2.5)
        print("Maybe you can find something on the island that would work.")
        print("")
        time.sleep(2.5)
        print('"As if something like that would just drop from the sky" says your talkative squirrel friend.')
        print("")
        time.sleep(2.5)
        print('"Then again maybe it already has; to the north" suggests the squirrel.')
        print("")
        time.sleep(2.5)
        print("You take the squirrel's advice and head north again back towards the forest lake you found")
        print("")
        time.sleep(2.5)
        Lake()

    elif got_hammer_and_nails == False and got_parachute == False and got_planks == False:
        print("Wow, you have nothing at all that you need.")
        print("")
        time.sleep(2.5)
        print("Have you even been exploring this island?")
        print("")
        time.sleep(2.5)
        print('"I think you better turn around and do some exploring" says your talkative squirrel friend')
        print("")
        time.sleep(2.5)
        print("Unfortunatly you must heed the the squirrel's advice and you backtrack towards the forest lake you found")
        print("")
        time.sleep(2.5)
        Lake()




#------------------------ North Forest ----------------------------------

def north_forest():

    print("You walk along a little winding path going up into the high forest hills")
    print("")
    time.sleep(2.5) 
    print("The path eventually just ends in a bit of a dead end")
    print("")
    time.sleep(2.5) 
    print('Your just about to turn back, thinking; "that it was a giant waste of time".')
    print("")
    time.sleep(2.5) 
    print("When you spot a long dead parachuter hanging from one of the nearby trees")
    print("")
    time.sleep(2.5) 
    print("Unable to get down the parachuter had scratched their name into the bark of the tree")
    print("")
    time.sleep(2.5) 
    print('It simply reads "Reyanud waz ere".')
    print("")
    time.sleep(2.5) 
    print("You look at the parachute and it seems to be in good shape")
    print("")
    time.sleep(2.5) 
    print("That could certainly come in handy")
    print("")
    time.sleep(2.5) 
    global got_parachute
    got_parachute = True
    print("It takes a bit of time, but you are able to pull down the parachute from the tree, and roll it back into its bag")
    print("")
    time.sleep(3.5) 
    print("With the parachute added to the list of items your carrying around now, you head back to the forest lake")
    print("")
    time.sleep(4.5) 
    Lake()



#------------------------ Bear Cave ----------------------------------


def cave():
    print("You walk quickly through the cave, not wanting to spend a minute longer in here than you have to.")
    print("")
    time.sleep(3.5)
    print("As your rushing through, you practically trip over a long dead skeleton.")
    print("")
    time.sleep(2.5)
    print("You examine the corpse and notice an axe along with a blood splattered diary.")
    print("")
    time.sleep(2.5)
    print("You read the diary and find that it belonged to a fine warrior by the name of Kamil.")
    print("")
    time.sleep(3.5)
    print("Unfortuantly he thought that taking on a grizzly bear with an axe was a good idea.")
    print("")
    time.sleep(2.5)
    print("Your not going to do that, but that axe could come in handy.")
    print("")
    time.sleep(3.5)
    global got_axe
    got_axe = True
    print("You pick up the axe, slipping it through your belt for safe keeping.")
    print("")
    time.sleep(2.5)
    print("You waste no more time in the cave, dashing straight out and back into the 'Dense Jungle'.")
    print("")
    time.sleep(3)
    print("The bear gives you a bemused look as you run but, but does not chase you.")
    print("")
    time.sleep(2.5)
    jungle()


def tempt_with_honey():
    print("You suddenly remember the honeycomb that you took from the beehive.")
    print("")
    time.sleep(2.5)
    print("Your pretty sure bears like honey, right?")
    print("")
    time.sleep(2.5)
    print('"Pretty sure bears like like honey, genius." Says the Squirrel.')
    print("")
    time.sleep(2.5)
    print("You take the honeycomb and throw it towards the bear.")
    print("")
    time.sleep(2.5)
    print("The bear gives it a couple of quick sniffs and then tucks eagerly into the meal.")
    print("")
    time.sleep(2.5)
    print("While the bear is distracted you quickly run into the cave.")
    print("")
    time.sleep(2.5)
    cave()



def battle_or_run():
    print("Would you like to fight the bear, try to dash past the bear, or retreat south back into the 'Dense Jungle?'")
    print("")
    time.sleep(2.5)
    answer = input("Type: Fight, Dash, or Retreat ")

    if answer.lower() == "fight" or answer.lower() == "f" or answer.lower() == "yes" or answer.lower() == "y":
        print("Seriously?")
        print("")
        time.sleep(1.5)   
        print("Well it's your funeral.")
        print("")
        time.sleep(1.5)   
        print("You charge forward with your cutlass drawn.")
        print("")
        time.sleep(2.5)   
        print("The Grizzly looks a little bemused for a second before charging at you.")
        print("")
        time.sleep(2.5) 
        print("The full power of a large grizzly bear slams into you; knocking the weapon from your hands.")
        print("")
        time.sleep(2.5) 
        print("It then preceeds to take large chucks out of you with its powerful jaws.")
        print("")
        time.sleep(2.5) 
        print("You see your friend the Squirrel running up, and for a moment, hope soars in your heart.")
        print("")
        time.sleep(2.5) 
        print("The Squirrel takes one look at you, shakes its head, and runs back into the forest, leaving you to your terrible fate")
        print("")
        time.sleep(3.5) 
        print("Game Over")
        print("")
        time.sleep(2.5) 
        intro()

    elif answer.lower() == "dash" or answer.lower() == "d" or answer.lower() == "no" or answer.lower() == "n":
        print("You run as fast as you can past the bear.")
        print("")
        time.sleep(2.5)  
        num = random.randint(1,6)
        if num == 6:    
            print("The Grizzly looks a little bemused and doesn't attempt a chase.")
            print("")
            time.sleep(2.5)  
            print("You make it into the cave.")
            print("")
            time.sleep(2.5)  
            cave()
        else:
            print("The Grizzly looks a little bemused for a second before charging at you.")
            print("")
            time.sleep(2.5) 
            print("The full power of a large grizzly bear slams into you.")
            print("")
            time.sleep(2.5) 
            print("It then preceeds to take large chucks out of you with its powerful jaws.")
            print("")
            time.sleep(2.5) 
            print("You see your friend the Squirrel running up, and for a moment, hope soars in your heart.")
            print("")
            time.sleep(2.5) 
            print("The Squirrel takes one look at you, shakes its head, and runs back into the forest, leaving you to your terrible fate")
            print("")
            time.sleep(3.5) 
            print("Game Over")
            print("")
            time.sleep(2.5) 
            intro()

    elif answer.lower() == "retreat" or answer.lower() == "r":
        print('"Wow the human has used its brain for once, I\'ll note the date in my diary" Snarks the Squirrel.')
        print("")
        time.sleep(2.5)  
        print("You take the South path back to the 'Dense Jungle'")
        print("")
        time.sleep(2.5)  
        jungle()
    
    else:
        print("Sorry say that again")
        print("")
        time.sleep(2.5) 
        battle_or_run()


def bear_cave():
    print("As you leave the 'Dense Jungle' behind you, walking the path becomes much easier.")
    print("")
    time.sleep(2.5)
    print("As the trees becomer fewer and further between; you can make out cliffs rising up in front of you.")
    print("")
    time.sleep(3)
    print("At the base of the cliffs there seems to be an opening...")
    print("")
    time.sleep(2)
    print("Yes its a cave.")
    print("")
    time.sleep(1.5)
    print("As you approach the cave though, you suddenly hear a loud growl!")
    print("")
    time.sleep(2.5)
    print("A large grizzly bear comes stomping out of the cave, stopping you in your tracks")
    print("")
    time.sleep(2.5)
    print("Your not sure you want to tangle with large bear, but there might be something in the cave you need")
    print("")
    time.sleep(2.5)
    global got_honeycomb
    if got_honeycomb == True:
        tempt_with_honey()
    elif got_honeycomb == False:
        battle_or_run()




#------------------------ Forest Lake ----------------------------------


def navigation_Lake():
    print("Which way would you like to go?")
    print("")
    time.sleep(1.5)
    direction = input("North, West or South: ")
    if direction.lower() == "north" or direction.lower() == "n":
        print("You have decided to take the path that goes North")
        print("")
        time.sleep(2.5)
        print("loading... North Forest")
        print("")
        time.sleep(2.5)
        north_forest()

    elif direction.lower() == "east" or direction.lower() == "e":
        print("Squirel: oh my god!, im stuck on a deserted island with an idiot")
        print("")
        time.sleep(2.5)
        print("Squirel: ARE YOU BLIND, you... 'CANNOT' go that way!!!")
        print("")
        time.sleep(2.5)  
        navigation_Lake()

    elif direction.lower() == "south" or direction.lower() == "s":
        print("You have decided to take the path that goes South")
        print("")
        time.sleep(2.5)
        print("loading... East Beach")
        print("")
        time.sleep(2.5)    
        east_beach()

    elif direction.lower() == "west" or direction.lower() == "w":
        print("You have decided to go back towards West")
        print("")
        time.sleep(2.5)   
        print("loading... 'Dense Jungle'")
        print("")
        time.sleep(2.5)    
        jungle()

    else:
        print("I'm sorry I didn't understand that")
        print("")
        time.sleep(1)
        navigation_Lake()



def Lake():
    print()
    time.sleep(1)
    print("You finally make it to the end of the dense forest, you see light shinning through the large shrubs of grass.")
    print("")
    time.sleep(3)
    print("You break through the large shrubs of grass to reveal a large beautiful lake surrounded by trees.")
    print()
    time.sleep(2.5)
    print("The water in the lake is flowing water, indicating its drinkable.")
    print("")
    time.sleep(2.5)
    print("The water flows down from the mountain to the east of the trees")
    print()
    time.sleep(2.5)
    drink_water = input("Would you like to drink water: ")
    print()

    if drink_water == "yes" or drink_water == "Yes" or drink_water == "y":

        print("You pick up the water with you bare hand its nice and cold")
        print()
        time.sleep(2.5)
        print("You drink the water")
        print()
        time.sleep(2.5)
        print("You feel refreshed, and surprisingly energised")
        print()
        time.sleep(2.5)
        global your_health
        your_health =+ 15
        print("You gain 15HP")
        time.sleep(1.5)
        print()
        print("You also fill up your bottle for later use")
        time.sleep(2.5)
        print()

    elif drink_water == "no" or drink_water == "No" or drink_water == "n":
        print("You dont feel thirsty, however you fill your bottle up for later use")
        print()
    else:
        print("Squirrel: Hey man, i advise you drink the water")
        print()
        time.sleep(2.5)
        print("Squirrel: Or at least fill your bottle up")
        print()
        time.sleep(2.5)
        print("Squirrel: I know im a talking squirrel, but have i not advised you well before.")
        print()
        time.sleep(2.5)

    cut_wood = input("Would you like to cut the a tree for some wood: ")
    global got_axe
    if got_axe == True:
        print("The axe would be usefull to cut trees, its a good thing you brought the axe with you")

    elif got_axe == False:
        print("You need an axe to cut trees.")
        time.sleep(2.5)
        print()
        print("Explore other areas, to find something useful.")
        print()
        time.sleep(2.5)

    print()

    if (cut_wood == "yes" or cut_wood == "Yes" or cut_wood == "y") and got_axe == True:
        print("You grab your axe and proceed to the nearest tree")
        print()
        time.sleep(2.5)
        print("You strart chopping away at the tree, until the tree falls, nearly falling on top of you")
        print()
        time.sleep(2.5)
        print("You sigh in relief")
        print()
        time.sleep(2.5)
        print("You chop the tree into planks, and collect all of the planks that are usable.")
        print()
        global got_planks
        got_planks = True

    if (cut_wood == "yes" or cut_wood == "Yes" or cut_wood == "y") and got_axe == False:
        print("Squirrel: I dont think you have the facilities for that big man.")
        time.sleep(1.5)
        print("Squirrel: Look at you, all lost and wonderiing...")
        time.sleep(1.5)
        print("Squirrel: \"oh no, what am i gonna do now\", dont worry...")
        time.sleep(1.5)
        print("Squirrel: Ill give you another hint, its at the bear cave.")
        time.sleep(1.5)
        print("Squireel: You make me feel bad for making fun of you.")


    elif cut_wood == ("no" or cut_wood == "No" or cut_wood == "n") and got_axe == True:
        print("Squirrel: hey its me mister squirrel, look at meee!.")
        time.sleep(1.5)
        print()
        print("Squirrel: it wont hurt to collects some wood.")
        time.sleep(1.5)
        print("Squirrel: Its your choice, dont come crying to me later on.")
        time.sleep(1.5)
        print("Squirrel: Let me give you a hint... i believe it will be the last hint.")
        time.sleep(1.5)
        print()
        print("Squirrel: you should collect the wood from the trees, u might need it in the south.")
        time.sleep(1.5)
        print("Squirrel: Lucky you, i accidently gave you two hints>.")

    else:
        print("Squirrel: ohhh lord, please give me patience.")
        time.sleep(1.5)
        print("Squirrel: Please decide what your gonna do next.")
        time.sleep(1.5)
        print("Squirrel: Im getting very irritated, by your incompitance")
    print()
    print("Its time to go.")
    print()
    navigation_Lake()




#------------------------ Dense Jungle ----------------------------------


def navigation_jungle():
    print("Which way would you like to go?")
    print("")
    time.sleep(1.5)
    direction = input("North, East or South: ")
    if direction.lower() == "north" or direction.lower() == "n":
        print("You have decided to take the path that goes 'North'")
        print()
        time.sleep(2.5)
        print("loading... 'Bear Cave'")
        print()
        time.sleep(2.5)
        bear_cave()

    elif direction.lower() == "east" or direction.lower() == "e":
        print("You have decided to take the 'East' path")
        print()
        time.sleep(2.5)
        print("loading... 'Lake Forest'")
        print()
        time.sleep(2.5)
        Lake()

    elif direction.lower() == "south" or direction.lower() == "s":
        print("You have decided to go back 'South'")
        print()
        time.sleep(2.5)
        print("loading... 'Old Camp'")
        print()
        time.sleep(2.5)
        campsite_return()


    elif direction.lower() == "west" or direction.lower() == "w":
        print("Squirrel: oh my god!, im stuck on a deserted island with an idiot")
        print()
        time.sleep(2.5)   
        print("Squirrel: ARE YOU BLIND, you... 'CANNOT' go that way!!!")
        print()
        time.sleep(2.5)   
        navigation_jungle() 

    else:
        print("I'm sorry, I didn't understand that")
        print("")
        time.sleep(1)
        navigation_jungle()

def jungle():
    print("\n")
    print("\n")
    print("Ｄｅｎｓｅ Ｊｕｎｇｌｅ")
    time.sleep(2)
    print("\n")
    time.sleep(1.5)
    print("You have entered the 'Jungle'")
    print()
    time.sleep(2.5)
    print("The jungle is too dense, its coverd in shrubs and learge tree vines")
    print()
    time.sleep(2.5)
    print("Its only accessable, if u have a cutting tool")
    print()

    if got_cutlass == True:
        print("Luckily, you decided to carry the cutlass with you")
        print()
        time.sleep(2.5)
        print("with the cutlass, you cut through the 'Dense Jungle', cutting away at every shrub and tree vine that crosses your path")
        print()
        time.sleep(2.5) 
        print("You look around and see there are paths to the North, East and South")
        print("")
        time.sleep(2.5)
        navigation_jungle()
    elif got_cutlass == False:
        print("You dont have anything to cut the shrubs and vines, that cover the whole 'Dense Jungle'")
        print()
        time.sleep(2.5)
        print("Explore other areas of the map you might find something useful.")
        print()
        time.sleep(2.5)
        print("Squirrel: Whats with the long face, dont worry.")
        print()
        time.sleep(2.5)
        print("Squirrel: Your friendly neighbour hood squirel will give you hint!")
        print()
        time.sleep(2.5)
        print("Squirrel: The hint isss... Hut")
        print()
        time.sleep(2.5)
        print("With the less than subtle hint given you wander back to the campsite")
        print()
        time.sleep(2.5)
        campsite_return()

# -------------------------------Bridge----------------------------

def bridge():
    time.sleep(1.5)
    space_1= " -------------------------------------------------------------------"
    space_2= " -----  -------------  --------------  -------------  --------  ----"
    space_3= "     |  |           |  |            |  |           |  |      |  |   "
    space_4= "     |  |           |  |            |  |           |  |      |  |   "
    space_5= "     |  |           |  |            |  |           |  |      |  |   "
    space_6= "     |  |           |  |            |  |           |  |      |  |   "
    space_7= "     |  |           |  |            |  |           |  |      |  |   "
    space_8= "     |  |           |  |            |  |           |  |      |  |   "
    space_9= "     |  |           |  |            |  |           |  |      |  |   "
    space10= "_____----___________----____________----___________----______----___"
    space11= "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    space12= "____________________________________________________________________"
    print("{}".format(space_1))
    print("{}".format(space_2))
    print("{}".format(space_3))
    print("{}".format(space_4))
    print("{}".format(space_5))
    print("{}".format(space_6))
    print("{}".format(space_7))
    print("{}".format(space_8))
    print("{}".format(space_9))
    print("{}".format(space10))
    print("{}".format(space11))
    print("{}".format(space12))
    time.sleep(1.5)
    print()
    time.sleep(1.5)
    print("You made your way through the secret path, that was mentioned in the journal.")
    print()
    time.sleep(2.5)
    print("You walk for a few minuites, and see a bridge in very poor condition.")
    print()
    time.sleep(2.5)
    print("Your thinking if you should go through it or not.")
    print()
    time.sleep(2.5)
    print()
    print("Squirrel: Theres something very interesting ahead.")
    print()
    time.sleep(2.5)
    print("Squirrel: I say we go through to the other side.")
    time.sleep(2.5)
    print()
    print("You take the squirrels advise, and start to cross")
    time.sleep(2.5)
    print("")
    print("The panels are really bad and some fall away as you step on them.")
    time.sleep(2.5)
    print()
    print("But you still make it through to the other side.")
    time.sleep(2.5)
    print()
    print("loading... Secret Area")
    print()
    Secret_Area()
    print()


#------------------------Shipwreck Beach ----------------------------------

def navigation_shipwreck():       
    print("Which way would you like to go?")
    print("")
    time.sleep(1)
    direction = input("North or West? ")

    if direction.lower() == "north" or direction.lower() == "n":
        print("You take the North path back to the forest") 
        time.sleep(1)
        old_Hut()
          
    elif direction.lower() == "east" or direction.lower() == "e":
        print("You cannot go that way")
        time.sleep(1)
        navigation_shipwreck()

    elif direction.lower() == "south" or direction.lower() == "s":
        print("You have a little paddle in the sea, the cool water feels nice on your toes") 
        print("")
        time.sleep(3)
        print("Still, better move on now") 
        print("")
        time.sleep(2.5)
        navigation_shipwreck()
         

    elif direction.lower() == "west" or direction.lower() == "w":
        print("You take the West path along the beach")
        time.sleep(1) 
        skeleton_battle()       

    else:
        print("I'm sorry I didn't understand that")
        print("")
        time.sleep(1)
        navigation_shipwreck()


def shipwreck_beach():
    global got_hammer_and_nails
    if got_hammer_and_nails == False:

        print("\n")
        print("\n")
        print("\n")
        print("Ｓｈｉｐｗｒｅｃｋ")
        time.sleep(2)
        print("\n")


        print("As you leave the forest behind you, you come out onto another beach.")
        print("")
        time.sleep(2.5)  
        print("This is no sandy beach however, it is all pebbles and rocks.")
        print("")
        time.sleep(2.5)  
        print("And on the coastline you notice a large broken structure.")
        print("")
        time.sleep(2.5)  
        print("You begin walking towards it, and you realise its your ship that was wrecked.")
        print("")
        time.sleep(2.5)  
        print('Sure enough; as you come alongside it, you can read the name "The Code Nation"')
        print("")
        time.sleep(2.5)  
        print("You assess its viability as a sailing vessel, but its really beat up.")
        print("")
        time.sleep(2.5)  
        print('"Your not thinking of repairing that are you?" The Squirrel starts.')
        print("")
        time.sleep(2.5) 
        print('"You would have better luck sailing a child\'s floatation ring out of here." The Squirrel quips.')
        print("")
        time.sleep(2.5) 
        print("You realise this sodden, broken thing is beyond repair.")
        print("")
        time.sleep(2.5)  
        print("Despite that, you have a look around for anything useful.")
        print("")
        time.sleep(2.5)  
        print("You come across a rusty old hammer and some nails in a bag.")
        print("")
        time.sleep(2.5)  
        got_hammer_and_nails = True
        print("You stuff these into your jacket pockets, they may be useful somewhere.")
        print("")
        time.sleep(2.5)
        print("With the wreck salvaged; you look around for where to head next.")
        print("")
        time.sleep(2.5) 
        print("The beach to the east is blocked off by large rocks and of course the open sea is to the south.")
        print("")
        time.sleep(2.5) 
        print("You can carry on down the beach to the west or head back north to the forest?")
        print("")
        time.sleep(2.5) 
        navigation_shipwreck()
    elif got_hammer_and_nails == True:
        print("Your back on the beach near your shipwreck")
        print("")
        time.sleep(2.5) 
        print("The beach to the east is blocked off by large rocks and of course the open sea is to the south.")
        print("")
        time.sleep(2.5) 
        print("You can carry on down the beach to the west or head back north to the forest?")
        print("")
        time.sleep(2.5) 
        navigation_shipwreck()





#------------------------Skeleton Battle ----------------------------------



def outro():
    print("With the skeleton defeated you look around for paths you can take.")
    print("")
    time.sleep(2.5) 
    if given_clue == True:
        print("You scan the rock face and notice a tiny gap which you might just be able to squeeze through.")
        print("")
        time.sleep(2.5)  
        bridge()

    elif given_clue == False:
        print("You scan the rock face but there doesn't seem to be any way past it.")
        print("")
        time.sleep(2.5)  
        print("The only way left to go is back to your shipwreck.")
        print("")
        time.sleep(2.5) 
        print("Still at least you have a bottle of rum now, I wonder what you can use it for?")
        print("")
        time.sleep(2.5) 
        shipwreck_beach()


def next_round_of_battle_p():
    print("You both regain your stance, and circle each other once again, looking for an opening to attack.")
    print("")
    time.sleep(2.5) 
    print("Will you attack now or wait for your opponents next move?")
    print("")
    time.sleep(2.5) 
    move1 = input("Attack or Wait? " )
    if move1.lower() == "attack" or move1.lower() == "a" or move1.lower() == "yes" or move1.lower() == "y" :
        battle_chance_p_a()
    elif move1.lower() == "wait" or move1.lower() == "w" or move1.lower() == "no" or move1.lower() == "n" :
        battle_chance_p_w()
    else:
        print("While your dithering the pirate comes at you quickly and slashes at your arm")
        print("")
        time.sleep(1.5)
        print("The sharp blade pierces your shoulder and you stumble back wounded")
        print("")
        time.sleep(1.5)
        global your_health
        your_health -= 25
        print("You lose 25HP")
        print("")
        time.sleep(2.5)
        health_check_p()




def health_check_p():
    global your_health
    global pirates_health
    if your_health <= 0:
        print("The pirate's last has attack, has left you mortally wounded.")
        print("")
        time.sleep(2.5)
        print("You collapse down to the ground; bleeding heavily from your wounds.")
        print("")
        time.sleep(2.5)
        print("As your vision fades, you sense the skeleton standing above you.")
        print("")
        time.sleep(2.5)
        print('"Arrr no one bests Cut-throat Dan" he says, "Now I\'ll be takin my clothes back if ye don\'t mind"')
        print("")
        time.sleep(2.5)
        print("Game Over!")
        print("")
        intro()
    elif pirates_health <= 0:
        print("Your last attack has left the skeleton mortally wounded.")
        print("")
        time.sleep(2.5)
        print("He drops his sword; which shatters on the ground. But strangly, he places the rum bottle down so it wont break and gives you one last evil look.")
        print("")
        time.sleep(2.5)
        print('"Curse you" he spits, "You have bested me"')
        print("")
        time.sleep(2.5)
        print("His skeleton stops magically animating and his bones scatter to the wind")
        print("")
        time.sleep(2.5)
        global got_rum_bottle
        got_rum_bottle = True
        print("You walk over to his discarded rum bottle and pick it up")
        print("")
        outro()
    else:
        next_round_of_battle_p()



def battle_chance_p_a():
    chance1 = random.randint(1, 3)
    if chance1 == 1:
        print("You lunge forward with your cutlass, but the pirate knocks your blade away and counters with stab of his own")
        print("")
        time.sleep(2.5)
        print("The sharp blade pierces your shoulder and you stumble back wounded")
        print("")
        time.sleep(1.5)
        global your_health
        your_health -= 25
        print("You lose 25HP")
        print("")
        time.sleep(2.5)
        health_check_p()
    else:
        print("You lunge forward with your cutlass, and the pirate misses his parry.")
        print("")
        time.sleep(2.5)
        print("Your blade pierces his bones and he stumbles back wounded.")
        print("")
        time.sleep(1.5)
        global pirates_health
        pirates_health -= 25
        print("He loses 25HP")
        print("")
        time.sleep(2.5)
        health_check_p()


def battle_chance_p_w():
    chance2 = random.randint(1, 4)
    if chance2 == 1:
        print("You wait patiently for the skeleton to attack, when he does you attempt a parry.")
        print("")
        time.sleep(2.5)
        print("You fumble the block and the skeleton's sword finds its mark.")
        print("")
        time.sleep(2.5)
        print("The sharp blade pierces your shoulder and you stumble back wounded.")
        print("")
        time.sleep(1.5)
        global your_health
        your_health -= 25
        print("You lose 25HP")
        print("")
        time.sleep(2.5)
        health_check_p()
    else:
        print("You wait patiently for the skeleton to attack, when he does you attempt a parry.")
        print("")
        time.sleep(2.5)
        print("You deftly knock the pirate's blade aside, and thurst your own into his chest.")
        print("")
        time.sleep(2.5)
        print("Your blade pierces his bones and he stumbles back wounded.")
        print("")
        time.sleep(1.5)
        global pirates_health
        pirates_health -= 25
        print("He loses lose 25HP")
        print("")
        time.sleep(2.5)
        health_check_p()



def fight():
    print("You draw your cutlass and take up a fighting stance opposite the animated skeleton.")
    print("")
    time.sleep(2.5) 
    print("You circle each other looking for an opening to attack.")
    print("")
    time.sleep(2.5) 
    print("Will you attack first or wait for your opponents move?")
    print("")
    time.sleep(2.5) 
    move1 = input("Attack or Wait? " )
    if move1.lower() == "attack" or move1.lower() == "a" or move1.lower() == "yes" or move1.lower() == "y" :
        battle_chance_p_a()
    elif move1.lower() == "wait" or move1.lower() == "w" or move1.lower() == "no" or move1.lower() == "n" :
        battle_chance_p_w()
    else:
        print("While your dithering the pirate comes at you quickly and slashes at your arm")
        print("")
        time.sleep(1.5)
        print("The sharp blade pierces your shoulder and you stumble back wounded")
        print("")
        time.sleep(1.5)
        global your_health
        your_health -= 25
        print("You lose 25HP")
        print("")
        time.sleep(2.5)
        health_check_p()


def fight_preamble():
    print("Will you fight the skeleton pirate or run away?")
    print("")
    time.sleep(2.5) 
    decision = input("Fight or Run? ")
    print("")
    if decision.lower() == "fight" or decision.lower() == "fight the skeleton" or decision.lower() == "f" or decision.lower() == "attack" or decision.lower() == "battle" or decision.lower() == "yes" or decision.lower() == "y":
        print("You decide to fight Cut-throat Dan")
        print("")
        time.sleep(2.5) 

        if got_cutlass == False:
            print("With no weapon!")
            print("")
            time.sleep(2.5) 
            print("Are you kidding!")
            print("")
            time.sleep(2.5) 
            print("You best run away.")
            print("")
            time.sleep(2.5) 
            print("You turn tail and run back down the beach")
            print("")
            time.sleep(2.5)
            print('You glance backwards expecting that the skeleton will chase you')
            print("")
            time.sleep(2.5) 
            print('But he is just chuckling to himself, and yells after you "Go on run! You yellow-bellied rat"')
            print("")
            time.sleep(2.5) 
            print('"But you will be back here to face me, mark my words". And with that he takes a swig from his rum bottle and sits back down against the cliff face')
            print("")
            time.sleep(2.5) 
            print("You're Glad to be out of range of that monster but now you have to backtrack towards your shipwreck ")
            print("")
            time.sleep(2.5) 
            shipwreck_beach()

        elif got_cutlass == True:
            fight()

    elif decision.lower() == "run" or decision.lower() == "run away" or decision.lower() == "r" or decision.lower() == "flee" or decision.lower() == "flee for your life" or decision.lower() == "no" or decision.lower() == "n":
        print("You turn tail and run back down the beach")
        print("")
        time.sleep(2.5)
        print('You glance backwards expecting that the skeleton will chase you')
        print("")
        time.sleep(2.5) 
        print('But he is just chuckling to himself, and yells after you "Go on run! You yellow-bellied rat"')
        print("")
        time.sleep(2.5) 
        print('"But you will be back here to face me, mark my words". And with that he takes a swig from his rum bottle and sits back down against the cliff face')
        print("")
        time.sleep(2.5) 
        print("You're Glad to be out of range of that monster but now you have to backtrack towards your shipwreck ")
        print("")
        time.sleep(2.5) 
        shipwreck_beach()
    else:
        print("I didn't understand that, were your hands shaking with fear?")
        print("")
        time.sleep(2.5) 
        fight_preamble()


def skeleton_battle():
    print("You find yourself on a long thin beach that streches out into the distance")
    print("")
    time.sleep(2.5)
    print("Its quite picturesque, you would stand and stare at the view in better circumstances")
    print("")
    time.sleep(2.5)
    print("You walk along the beach, looking out for any useful items that may have washed up.")
    print("")
    time.sleep(2.5)
    print("There doesn't seem to be much here, and a few meters further ahead the beach ends at a sheer cliff face.")
    print("")
    time.sleep(2.5)
    print("As you get closer to the cliff face, you see an ancient skeleton propped up against the rocks.")
    print("")
    time.sleep(2.5)
    print("Its clothes are in tatters, but you recognise the attire, and the rum bottle it has clasped in its hands, confirms your suspicions.")
    print("")
    time.sleep(2.5)
    print("He was a pirate!")
    print("")
    time.sleep(2.5)
    print("Then, to your utter astonishment, the skeleton pirate begins to rise.")
    print("")
    time.sleep(2.5)
    print("As it lifts itself up, its tired bones creak, and sand flows from its ribcage back onto the beach.")
    print("")
    time.sleep(2.5)
    print("When it is stood fully upright, its face looks up at you and its empty eyesockets seem to lock onto you.")
    print("")
    time.sleep(2.5)
    print('You nearly jump out of your skin when he bellows "I be Cut-throat Dan, and that be my hat and coat ye be wearin.')
    print("")
    time.sleep(2.5)
    print('He unsheathes a wicked looking sabre and points it towards you, saying: "I\'ll be takin those off your corpse you slimey cur"')
    print("")
    time.sleep(2.5)
    fight_preamble()





# -------------------------- Mushroom Forest ------------------------------------------

def navigation_mushrooms_forest():
    print("Which way would you like to go?")
    print("")
    time.sleep(1)
    direction = input("North or South? ")
    if direction.lower() == "north" or direction.lower() == "n":
        print("You take the North path")
        time.sleep(1)
        bee_hive_area()

    elif direction.lower() == "east" or direction.lower() == "e":
        print("You cannot go that way")
        time.sleep(1)
        navigation_mushrooms_forest()

    elif direction.lower() == "south" or direction.lower() == "s":
        print("You take the South path")
        time.sleep(1) 
        old_Hut()
           
    elif direction.lower() == "west" or direction.lower() == "w":
        print("You cannot go that way") 
        time.sleep(1)    
        navigation_mushrooms_forest()

    else:
        print("I'm sorry I didn't understand that")
        print("")
        time.sleep(1)
        navigation_mushrooms_forest()

def moving_on():
    print("You have a look around, the forest to the west is impassable, and the area to the East ends in a sheer cliff")
    print("")
    time.sleep(3) 
    print("There does seem to be a way through the forest to the north, or you can go back to the south")
    print("")
    time.sleep(3) 
    navigation_mushrooms_forest()



def pick_mushroom():

    num = random.randint(1,6)
    if num == 1:
        print("You pick some small, thin orange capped mushrooms and eat them.")
        print("")
        time.sleep(2.5)     
        print("Urg! Bad Idea!")
        print("")
        time.sleep(2.5)     
        print("Your mouth is burning and you cannot stop yourself from bringing the mushrooms back up.")
        print("")
        time.sleep(2.5) 
        global your_health
        your_health -= 40
        print("You lose 40HP.")
        print("")
        time.sleep(2.5) 
        print("After vomiting your deadly meal back up, you lie on the ground for a while and try to recover your strength.")
        print("")
        time.sleep(3)  
        print('After a while the squirrel scratches your face and says "Better get moving genius".')
        print("")
        time.sleep(2.5) 
        print("You have had enough mushrooms for one day so you move straight on out of the area.")
        print("")
        time.sleep(2.5) 
        moving_on()

    elif num == 2:
        print("You pick some small, really thin mushrooms, with grey tops, and eat them.")
        print("")
        time.sleep(2.5)     
        print("The world starts to go a little weird")
        print("")
        time.sleep(2.5)   
        print("Suddenly its not only the squirrel talking but all of the trees as well")
        print("")
        time.sleep(2.5)  
        print("You sit on the grass and have a lovely conversation with the forest")
        print("")
        time.sleep(2.5)  
        print("One particulary nice tree tells you about a secret passage guarded by a pirate skeleton")
        print("")
        time.sleep(2.5) 
        global given_clue
        given_clue = True 
        print("The other trees seem angry that their sectret has been passed on")
        print("")
        time.sleep(2.5) 
        print("So you decide to wander on, your stomach a little fuller and your heart a little lighter")
        print("")
        time.sleep(3) 
        your_health += 10
        print("You gain 10HP")
        print("")
        time.sleep(2.5) 
        moving_on()

    elif num > 2:
        print("You pick some medium sized, white stemmed mushrooms, and eat them.")
        print("")
        time.sleep(2.5)     
        print("You seem to have chosen wizely, your hunger is certainly abating")
        print("")
        time.sleep(2.5)   
        your_health += 10
        print("You gain 10HP")
        print("")
        time.sleep(2.5)
        print("With your stomach a little fuller you decide to continue onwards")
        print("")
        time.sleep(3) 
        moving_on()


def eat_mushrooms():
    print("Do you want to risk it and eat some mushrooms?")
    print("")
    time.sleep(2.5)
    answer = input("Yes or No ?")
    if answer.lower() == "yes" or answer.lower() == "y":
        pick_mushroom()
    elif answer.lower() == "no" or answer.lower() == "n":
        print("Well thats probably safer but your hunger is only going to get worse now")
        print("")
        time.sleep(2.5) 
        global your_health
        your_health -= 15
        print("You lose 15HP from dealing with your hunger")
        print("")
        time.sleep(2.5)
        moving_on()
    else:
        print("Pardon?")
        print("")
        time.sleep(2.5)
        eat_mushrooms()

def mushroom_forest():
    global times_in_mush_forest
    if times_in_mush_forest == 0:
        print("You make your way slowly through the forest")
        print("")
        time.sleep(2.5)
        print("As you continue forwards the trees begin to thin out a little")
        print("")
        time.sleep(2.5)
        print("You find yourself in a little clearing, with the sunlight beaming down onto bright green grass")
        print("")
        time.sleep(2.5)
        print("All around the edges of the clearing are various types of mushrooms growing at the bottom of the trees")
        print("")
        time.sleep(2.5)
        print("Your stomach suddenly lets out a loud growl and you realise you are starving")
        print("")
        time.sleep(2.5)
        print("You are not much of a botanist though, you have no idea if they are poisonous or not")
        print("")
        time.sleep(2.5)
        times_in_mush_forest = 1
        eat_mushrooms()
    else:
        print("You find yourself back in the mushroom forest.")
        print("")
        time.sleep(2.5)
        print("You don't feel like eating any mushrooms now.")
        print("")
        time.sleep(2.5)
        moving_on()

# ----------------- Old Hut -----------------------------------

def navigation_old_hut():
    direction = input("North, East or South: ")
    if direction.lower() == "north" or direction.lower() == "n":
        print("You have decided to take the path that goes North")
        print()
        time.sleep(2.5)
        print("loading... Forest with mushrooms")
        print()
        time.sleep(2.5)
        mushroom_forest()

    elif direction.lower() == "east" or direction.lower() == "e":
        print("You have decided to the East path")
        print()
        time.sleep(2.5)
        print("loading... Old Campsite")
        print()
        time.sleep(2.5)
        campsite_return()

    elif direction.lower() == "south" or direction.lower() == "s":
        print("You have decided take the South path")
        print()
        time.sleep(2.5)
        print("loading... Beach with shipwreck")
        print()
        time.sleep(2.5)
        shipwreck_beach()

    elif direction.lower() == "west" or direction.lower() == "w":
        print("You cannot go that way")
        print()
        time.sleep(1.5)
        navigation_old_hut()
    else:
        print("Excuse me?")
        print()
        time.sleep(1.5)
        navigation_old_hut()


def left_path():
    print("You chose left.")
    print()
    time.sleep(2)
    print("Great Choice! You have gained a cutlass which will aid in your cutting abilities and fighting enemies.")
    print()
    time.sleep(3)
    global got_cutlass
    got_cutlass = True
    print("You look around, as well as the path back east, there are paths to the north or south?")
    print()
    print("")
    time.sleep(2.5)
    print("Which way would you like to go?")
    print("")
    time.sleep(1.5)
    navigation_old_hut()


def right_path():
    print("You chose right.")
    print()
    time.sleep(2)
    print("Great Choice! You have uncovered a Journal unveiling the secrets of the island.")
    print()
    global given_clue
    given_clue = True
    time.sleep(3)
    print('Squirrel - "No way are we leaving the cutlass behind!')
    print()
    time.sleep(2)
    print("The Squirrel yanks the cutlass, which cuts you as it falls")
    print()
    time.sleep(2)
    global your_health
    your_health -= 10
    print("Lose 10HP")
    print()
    time.sleep(2)
    global got_cutlass
    got_cutlass = True
    print("But gain a cutlass")
    print()
    time.sleep(2)
    print("You look around, as well as the path back east, there are paths to the north or south?")
    print()
    print("")
    time.sleep(3.5)
    print("Which way would you like to go?")
    print("")
    time.sleep(2.5)
    navigation_old_hut()


def decision():
    print("You may only retrieve one item: 'type left for Cutlass or type right for Journal.'")
    print()
    time.sleep(3)
    left_or_right = input("Which one do you want to choose? [L/R]: ")

    if left_or_right.upper() == "L" or left_or_right.upper() == "LEFT":
        left_path()
        time.sleep(2)
    elif left_or_right.upper() == "R" or left_or_right.upper() == "RIGHT":
        right_path()
        time.sleep(2)
    else:
        time.sleep(2)
        print("Invalid input, try again.")
        time.sleep(2)
        decision()

def old_Hut():
    global got_cutlass
    if got_cutlass == False:
        
        print("\n")
        print("\n")
        print("Ｏｌｄ Ｈｕｔ")
        time.sleep(2)
        print("\n")

        print("You have arrived to the Forest, You can enter the hut by the river.")
        print()
        time.sleep(2.5)
        print("You keep moving forward and find the corpse of Nice Nasra, the friendly skeleton.")
        print()
        time.sleep(2.5)
        print("In her hand is a cutlass and by her side is a Journal.")
        print()
        time.sleep(2.5)
        decision()

    elif got_cutlass == True:
        print("You have arrived back to the Forest hut by the river.")
        print()
        time.sleep(2.5)
        print("You look around, as well as the path back east, there are paths to the north or south?")
        print()
        print("")
        time.sleep(2.5)
        print("Which way would you like to go?")
        print("")
        time.sleep(1.5)
        navigation_old_hut()




# ----------------- Intro -------------------------------------

def name(): 
        global name    
        name = input("What is your name? ")
        time.sleep(1)
        print(f"Hello {name}, I hope your ready for an exciting game. :D")
        time.sleep(2)
        start_game()
        
def print_slow(str):
        for char in str:
            time.sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()



print("PEGI 18")
time.sleep(2.5)
print("\n")
print("A TEAM 4 GAME")
time.sleep(2.5)
print("\n")
print("DOLBY SURROUND SOUND")
time.sleep(2.5)
print("\n")
print("LUCAS 'ART'")
time.sleep(2.5)
print("\n")
print("\n")
print("""
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░███
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░▄▀▄▀░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█░░▄▀░░████░░▄▀░░███░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀░░█████████░░▄▀░░██░░▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░███░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█
█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░███░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░░░░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░███░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█
█████████░░▄▀░░█░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░█████████░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀░░█████████░░▄▀░░██░░▄▀░░█
█░░░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░░░▄▀░░░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░▄▀▄▀░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀░░░░█
█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░█░░░░░░█████████░░░░░░██░░░░░░██░░░░░░█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░███
████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████""""")
time.sleep(2.5)
print("\n")

skeleton = ("""LOADING...
            _..--""---.
          /           ".
          `            l
          |'._  ,._ l/"\.
          |  _J<__/.v._/
           \( ,~._,,,,-)
            `-\' \`,,j|
               \_,____J
          .--.__)--(__.--.
         /  `-----..--'. j
         '.- '`--` `--' \\
        //  '`---'`  `-' \\
       //   '`----'`.-.-' \\
     _//     `--- -'   \' | \________
    |  |         ) (      `.__.---- -'\\
     \7          \`-(               74\\
     ||       _  /`-(               l|//7__
     |l    ('  `-)-/_.--.          f''` -.-"|
     |\     l\_  `-'    .'         |     |  |
     llJ   _ _)J--._.-('           |     |  l
     |||( ( '_)_  .l   ". _    ..__I     |  L
     ^\\\||`'   "   '"-. " )''`'---'     L.-'`-.._
          \ |           ) /.              ``'`-.._``-.
          l l          / / |                      |''|
           " \        / /   "-..__                |  |
           | |       / /          1       ,- t-...J_.'
           | |      / /           |       |  |
           J  \  /"  (            l       |  |
           | ().'`-()/            |       |  |
          _.-"_.____/             l       l.-l
      _.-"_.+"|                  /        \.  \.
/"\.-"_.-"  | |                 /          \   \.
\_   "      | |                1            | `'|
  |ll       | |                |            i   |
  \\\       |-\               \j ..          L,,'. `/
 __\\\     ( .-\           .--'    ``--../..'      '-..
   `'''`----`\\\\ .....--'''
              \\\\                         
""")
for char in skeleton:
    sleep(0.00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
    sys.stdout.write(char)
    sys.stdout.flush()



def old_cabin2():
        print_slow("Squirrel - Right! That was a lot of fun, but you need to stop wasting time! \n\nSquirrel - If your still here by nightfall, your fair game to the 'skeletons' and other 'woodland critters' on the island. \n\nSquirrel - Currently your in a 'Safe Area.'")
        time.sleep(1)
        print("\n")
        print_slow("Squirrel - From here, you can go 'North' to the 'Dense Jungle'...\n\nSquirrel- Or 'West' to the 'Old Hut,' ")
        navigation_camp()

def squirrel_potion():
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠉⠉⠀⠀⠀⠈⠑⢢⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⢀
⠀⠀⠀⣀⣠⠤⠤⠤⠤⠤⣶⣉⣹⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⣰⠚
⣠⣞⣋⠁⣤⣴⣷⣶⢤⠀⠸⢫⠃⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣆⠀⠀⠀⠀⠀⠀⠀⡟⠉⠀⠀
⡏⠁⠈⠱⡙⢿⣿⣽⣗⠇⠀⠸⠟⢻⣀⣀⣀⠀⠀⠀⠀⠀⠀⢀⡀⠤⠤⠤⠤⠤⠤⢀⣀⠀⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀
⠹⣦⣀⡤⢣⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠒⠒⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⣄⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⢷⠀⠀
⠀⠈⠓⢄⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⢸⠀⠀⠀⠀⠀⠀⠸⠀⠀
⠀⠀⠀⠀⠑⠢⢍⡒⠀⠠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⢣⣀⡼⠀⠀⠀⠀⠀⠀⠈⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠒⠊⠉⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢢⡀⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⢤⣸⠀⠀⠀⠀⠀⣆⠀⠀⢀⣀⠴⠚⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠙⢧⠀⠀⠀⠀⣏⠉⠉⠁⢀⣀⣀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠛⠒⠤⠤⠔⠊⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⠀⣸⠀⠀⠀⢰⠏⠉⠉⠉⠉⠳⣄⠈⠣⣀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⡤⠎⠀⢀⣤⡞⠁⠀⢀⡴⠁⠀⠀⠀⠀⢀⣤⣤⡭⣶⠞⠛⣲⡶⠖⠒⠚⠉⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠾⠿⠿⢤⣴⡶⠛⠉⠀⣠⠔⠉⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⣽⣛⣋⡀⠠⠤⠄⠒⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        time.sleep(1.5)
        print_slow(f"HAHAHAHAHA You didn't stand a chance {name}!!! My POWER LEVEL... ITS OVER 9000!!!")
        print("\n")
        print_slow(f"Squirrel - Here {name}, Take this potion...(Hands yellow potion) \n\n('YUCKKK...SOUR'...Your health fully returns, but you feel sick and euphoric)")
        global your_health
        your_health = 100
        print("\n")
        old_cabin2()
         
def next_round_of_battle():
    print_slow("You both regain your stance")
    print("\n")
    print_slow("Will you attack now or wait for your opponents next move?")
    print("\n")
    move1 = input("Attack or Wait? " )
    if move1.lower() == "attack" or move1.lower() == "a" or move1.lower() == "yes" or move1.lower() == "y" :
        battle_chance_a()
    elif move1.lower() == "wait" or move1.lower() == "w" or move1.lower() == "no" or move1.lower() == "n" :
        battle_chance_w()
    else:
        print_slow("While your messing about the squirrel comes at you quickly and Kicks you in the nuts!")
        print("\n")
        print_slow("Struggling to take another breathe, you drop to your knees!")
        print("\n")
        global your_health
        your_health -= 100
        print("You lose 100HP")
        print("\n")
        health_check()

def health_check():
    global your_health
    global squirrel_health
    if your_health <= 0:
        print_slow("The squirrels slap has left you on your knees, unable to fight. ")
        print("\n")
        squirrel_potion()
    elif squirrel_health <= 0:
        print_slow("Your last attack has left the squirrel mortally wounded.")
        print("\n")
        print_slow("He gets back up with a sinister look on his face, licks his lips and climbs up onto your shoulder")
        print("\n")
        old_cabin2()
    else:
        next_round_of_battle()

def battle_chance_a():
    chance1 = random.randint(1, 2)
    if chance1 == 1:
        print_slow("The squirrel slaps you back into next week!")
        print("\n")
        print_slow("You stumble back")
        print("\n")
        global your_health
        your_health -= 50
        print_slow("You lose 50HP")
        print("\n")
        health_check()
    else:
        print_slow("You lunge forward giving a swift kick to the head...")
        print("\n")
        print_slow("Your barefoot barely does any damage...")
        print("\n")
        global squirrel_health
        squirrel_health -= 15
        print_slow("He loses 15HP")
        print("\n")
        health_check()

def battle_chance_w():
    chance2 = random.randint(1, 4)
    if chance2 <= 4:
        print_slow("You wait for the squirrel to attack, when he does you attempt to block...")
        print("\n")
        print_slow("You fumble the block and the squirrel slaps you down again...")
        print("\n")
        print_slow("The tiny hand pierces your cheek...")
        print("\n")
        global your_health
        your_health -= 40
        print_slow("You lose 40HP")
        print("\n")
        health_check()
    else:
        print_slow("You wait for the squirrel to attack, when he does you attempt a block...")
        print("\n")
        print_slow("You awkwardly knock the squirrels leathery palm aside, and thurst your elbow into his whiskers...")
        print("\n")
        global squirrel_health
        squirrel_health -= 15
        print_slow("He loses 15HP")
        print("\n")
        health_check()

def pre_fight():
    print_slow("The Squirrel puts up his fists and starts throwing shapes.")
    print("\n")
    print_slow("You put your fists up and circle each other...you are somewhat confused, but it would seem the squirrel means business...")
    print("\n") 
    print_slow("Will you attack first or wait for your opponents move?")
    print("\n")  
    move1 = input("Attack or Wait? " )
    if move1.lower() == "attack" or move1.lower() == "a" or move1.lower() == "yes" or move1.lower() == "y" :
        battle_chance_a()
    elif move1.lower() == "wait" or move1.lower() == "w" or move1.lower() == "no" or move1.lower() == "n" :
        battle_chance_w()
    else:
        print_slow("While your messing about the squirrel comes at you quickly! HADOUKEN!")
        print("\n")
        print_slow("His tiny little leathery palm feels disgusting while it punches a hole through your chest...")
        print("\n")
        global your_health
        your_health -= 100
        print("You lose 100HP")
        print("\n")
        health_check()
        
def Old_Campsite():
        print("Ｏｌｄ Ｃａｍｐｓｉｔｅ")
        time.sleep(1.5)
        print("\n")
        print_slow("You have stumbled across an old run down campsite, It looks like it hasn't been used since Pirates roamed the Seas!...")
        print("\n")
        print_slow("You start to rummage around frantically, in the hopes of finding something to eat or drink...")
        print("\n")
        print("ALAS!")
        print_slow("...An empty bottle ")
        print_slow("(This may come in handy later)")
        print("\n")
        print_slow("You realise your naked!")
        print("\n")
        print_slow("Luckily in a near by tent, you find a 'Pirate hat','Pirate coat' and some 'long Johns'")
        print("\n")
        print_slow("As you leave the tent with your new attire, You spot a patch of mushrooms! \n\nThank God! \n\nFamished, you run over and scoff the mushrooms down without a seconds thought... \n\nYour head starts spinning")
        print("\n")
        print_slow("A feeling of dread washes over you...but then...")
        print("\n")
        print_slow("You hear a voice")
        print("\n")
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠉⠉⠀⠀⠀⠈⠑⢢⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⢀
⠀⠀⠀⣀⣠⠤⠤⠤⠤⠤⣶⣉⣹⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⣰⠚
⣠⣞⣋⠁⣤⣴⣷⣶⢤⠀⠸⢫⠃⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣆⠀⠀⠀⠀⠀⠀⠀⡟⠉⠀⠀
⡏⠁⠈⠱⡙⢿⣿⣽⣗⠇⠀⠸⠟⢻⣀⣀⣀⠀⠀⠀⠀⠀⠀⢀⡀⠤⠤⠤⠤⠤⠤⢀⣀⠀⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀
⠹⣦⣀⡤⢣⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠒⠒⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⣄⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⢷⠀⠀
⠀⠈⠓⢄⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⢸⠀⠀⠀⠀⠀⠀⠸⠀⠀
⠀⠀⠀⠀⠑⠢⢍⡒⠀⠠⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⢣⣀⡼⠀⠀⠀⠀⠀⠀⠈⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠒⠊⠉⠀⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢢⡀⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⢤⣸⠀⠀⠀⠀⠀⣆⠀⠀⢀⣀⠴⠚⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠙⢧⠀⠀⠀⠀⣏⠉⠉⠁⢀⣀⣀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠛⠒⠤⠤⠔⠊⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⠀⣸⠀⠀⠀⢰⠏⠉⠉⠉⠉⠳⣄⠈⠣⣀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⡤⠎⠀⢀⣤⡞⠁⠀⢀⡴⠁⠀⠀⠀⠀⢀⣤⣤⡭⣶⠞⠛⣲⡶⠖⠒⠚⠉⣳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠾⠿⠿⢤⣴⡶⠛⠉⠀⣠⠔⠉⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⣽⣛⣋⡀⠠⠤⠄⠒⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        time.sleep(1.5)
        print_slow(f"Squirrel - Hey! There {name}, I've been waiting sooooo long for someone to come and play with me! \nSquirrel - My only companion has been this rock I named 'Stone'")
        time.sleep(2)
        print("\n")
        print("\n")
        print("ＦＩＧＨＴ！")
        print("\n")
        pre_fight()

def start_game():
        print("\n")
        print("\n")
        print("Ｔｈｅ Ｂｅａｃｈ")
        time.sleep(2)
        print("\n")
        print_slow("'You awaken, dazed and confused. The sun so bright it takes a minute for your eyes to adjust.'")
        time.sleep(2)
        print("\n")
        print_slow("'You climb to your feet and take a look around only to discover your on a beach, no clue as to how you got there'")
        time.sleep(2)
        print("\n")
        print_slow("'The only thing you have with you is your trusty compass necklace'")
        time.sleep(2)
        print("\n")
        print_slow("'In the distance you can see what looks to be an 'Old Campsite'")
        time.sleep(2)
        print("\n")
        print_slow("'Gingerly, you make your way over...'")
        time.sleep(2)
        print("\n")
        print("\n")
        Old_Campsite()

def intro():
    print("WARNING")
    time.sleep(3)
    print("\n")
    print("THIS GAME 'MAY' CONTAIN FLASHING LIGHTS AND IMAGES")
    time.sleep(3)
    print("\n")
    print("YOU HAVE BEEN WARNED")
    time.sleep(3)
    response = input("Do you wish to continue? [Y/N] ")

    if response.upper() == "Y" or response.upper() == "YES":
        time.sleep(2)
        print("EXCELLENT...")
        time.sleep(1)
        name()

    elif response.upper() == "N" or response.upper() == "NO":
        print("This is not the way.")
        time.sleep(2)
        intro()
        
    else:
        print("Try again, I didn't recognise that.")
        time.sleep(2)
        intro()

  
intro()