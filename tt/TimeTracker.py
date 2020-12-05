# importing necessary modules
from ttfunctions import *

import os

# Program Intro
print("\n\t\t\t\tTIME TRACKER", end="\n\t\t\t\t")
print("*" * 12, end="\n\n")

print("""
Hi there, Time Tracker here.\n
1. Start tracking
2. View saved data
3. Quit program 
""")

# lopping through to give users multiple chances if they input wrong data
while True:
    proceed = input("What would you like to do?(Please choose 1, 2 or 3) ")

    if proceed == "1":
        start_tracking()
        while True:
            request = input("\nWould you like to view your saved data?(Y or N): ")
            if request.lower() == "y":
                check_file = os.path.isfile("./timetracker.csv")
                if check_file:
                    view_data()
                else:
                    print("\nSorry you have no saved data yet. Start tracking to see your saved data!\n")
                break
            elif request.lower() == "n":
                print("\nThanks for using Time Tracker!❤\n")
                break
            else:
                print("Sorry didn't catch that please try again.\n")
        break          
    elif proceed == "2":
        check_file = os.path.isfile("./timetracker.csv")
        if check_file:
            view_data()
        else:
            print("\nSorry you have no saved data yet. Start tracking to see your saved data!\n")
        break
    elif proceed == "3":
        print("\nI'll be here when you need me😉. Goodbye.\n")
        break
    else:
        print("\nSorry you may have entered incorrect data please try again.\n")
