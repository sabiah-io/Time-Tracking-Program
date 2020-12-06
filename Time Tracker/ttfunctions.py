# importing necessary modules
from datetime import date
import csv
import os

def diff_mins(start_min, end_min):
    """
    Returns the absolute difference in minutes of the given arguments

    >>> total_mins(23, 12)
    >>> 11
    """
    total_min = abs(int(end_min) - int(start_min))
    return total_min



def start_tracking(date=date):
    """
    Keeps track of your input data and saves it in a .csv file

    """
    # requesting data to be used later
    print("\n\t\t\t\tTracking Data", end="\n\t\t\t\t")
    print("*" * 13, end="\n\n")
    start_hour = input("Enter start hour: ")
    start_min = input("Enter start minute(00 if you started exactly that hour): ")
    start_ampm = input("AM or PM: ")

    print("\n\n")

    end_hour = input("Enter end hour: ")
    end_min = input("Enter end minute(00 if you ended exactly that hour): ")
    end_ampm = input("AM or PM: ")


    # accounting for every possible bug that may affect dataframe structure
    try:
        if (int(start_hour) < 10) and (int(end_hour) < 10):
            try:
                if (int(start_min) < 10) and (int(end_min) < 10):
                    start_time = " " + start_hour + ":0" + start_min
                    end_time = " " + end_hour + ":0" + end_min
                elif int(start_min) < 10:
                    start_time = " " + start_hour + ":0" + start_min
                    end_time = " " + end_hour + ":" + end_min
                elif int(end_min) < 10:
                    end_time = " " + end_hour + ":0" + end_min
                    start_time = " " + start_hour + ":" + start_min
                else:
                    start_time = " " + start_hour + ":" + start_min
                    end_time = " " + end_hour + ":" + end_min
            except ValueError:
                print("\nSorry you may have entered incorrect data. Please restart the program.")
        elif int(start_hour) < 10:
            try:
                if (int(start_min) < 10) and (int(end_min) < 10):
                    start_time = " " + start_hour + ":0" + start_min
                    end_time = end_hour + ":0" + end_min
                elif int(start_min) < 10:
                    start_time = " " + start_hour + ":0" + start_min
                    end_time = end_hour + ":" + end_min
                elif int(end_min) < 10:
                    end_time = end_hour + ":0" + end_min
                    start_time = " " + start_hour + ":" + start_min
                else:
                    start_time = " " + start_hour + ":" + start_min
                    end_time = end_hour + ":" + end_min
            except ValueError:
                print("\nSorry you may have entered incorrect data. Please retart the program.")
        elif int(end_hour) < 10:
            try:
                if (int(start_min) < 10) and (int(end_min) < 10):
                    start_time = start_hour + ":0" + start_min
                    end_time = " " + end_hour + ":0" + end_min
                elif int(start_min) < 10:
                    start_time = start_hour + ":0" + start_min
                    end_time = " " + end_hour + ":" + end_min
                elif int(end_min) < 10:
                    end_time = " " + end_hour + ":0" + end_min
                    start_time = start_hour + ":" + start_min
                else:
                    start_time = start_hour + ":" + start_min
                    end_time = " " + end_hour + ":" + end_min
            except ValueError:
                print("\nSorry you may have entered incorrect data. Please restart the program.")
        else:
            try:
                if (int(start_min) < 10) and (int(end_min) < 10):
                    start_time = start_hour + ":0" + start_min
                    end_time = end_hour + ":0" + end_min
                elif int(start_min) < 10:
                    start_time = start_hour + ":0" + start_min
                    end_time = end_hour + ":" + end_min
                elif int(end_min) < 10:
                    end_time = end_hour + ":0" + end_min
                    start_time = start_hour + ":" + start_min
                else:
                    start_time = start_hour + ":" + start_min
                    end_time = end_hour + ":" + end_min
            except ValueError:
                print("\nSorry you may have entered incorrect data. Please retart the program.")
    except ValueError:
        print("\nSorry you may have entered incorrect data. Please restart the program.")


    # accepting data and writing to file
    if (start_ampm.lower() == "am" and end_ampm.lower() == "am") or  (start_ampm.lower() == "pm" and end_ampm.lower() == "pm"):

        # checking for value errors
        try:
            # if both starting and ending hours are "AM"
            total_hours = (int(end_hour) - int(start_hour))
            total_min = diff_mins(start_min, end_min)
            converted_total_hours = (total_hours * 60)
            total_mins = (total_min + converted_total_hours)
            amount_earned = round((total_mins / 60) * 5, 2)
            print("\nYou worked for a total of {}hour(s) {}min(s) and earned ${:.2f}!"
            .format(total_hours, total_min, amount_earned))
            print("Your data has been saved!\n")

            date = date.today()
            with open("timetracker.csv", "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([date, start_time, start_ampm.upper(), 
                end_time, end_ampm.upper(), total_hours, total_min, amount_earned])
        except ValueError:
            pass
    elif (start_ampm.lower() == "am" and end_ampm.lower() == "pm") or ((start_ampm.lower() == "pm" and end_ampm.lower() == "am")):
        
        try:
            # if starting hour is "AM" but ending hour is "PM" or vice versa
            if int(end_hour) == 12:
                total_hours = ((int(end_hour)) - int(start_hour))
            else:
                total_hours = ((int(end_hour) + 12) - int(start_hour))
            total_min = diff_mins(start_min, end_min)
            converted_total_hours = (total_hours * 60)
            total_mins = (total_min + converted_total_hours)
            amount_earned = round((total_mins / 60) * 5, 2)
            print("\nYou worked for a total of {}hour(s) {}min(s) and earned ${:.2f}!"
            .format(total_hours, total_min, amount_earned))
            print("Your data has been saved!\n")

            date = date.today()
            with open("timetracker.csv", "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([date, start_time, start_ampm.upper(), end_time, 
                end_ampm.upper(), total_hours, total_min, amount_earned])
        except ValueError:
            pass
    else:
        print("\nSorry you may have entered incorrect data. Please restart the program.")





def view_data():
    """
    Gives detailed information about saved data

    """
    with open("./timetracker.csv", "r", newline="") as fileX:
        # reading csv file
        reader = csv.reader(fileX)

        # designing dataframe for saved data
        print("\n\t\t\t\tSaved Data", end="\n\t\t\t\t")
        print("*" * 10, end="\n\n")
        print("Date", (" "*10)+"Start time", (" "*3)+"AM/PM", (" "*4)+"End time", 
        (" "*5)+"AM/PM", (" "*4)+"Hours", (" "*3)+"Mins", (" "*2)+"Amount earned($)")
        print("-" * 94)
        
        Total_hours = 0
        Total_mins = 0
        Total_amount = 0
        for row in reader:
            Total_hours += int(row[5])
            Total_mins += int(row[6])
            Total_amount += float(row[7])
            print("\n")
            for i in range(len(row)):
                print(row[i], end=" " * 8)

    print("\n\n\nTotal number of hours worked = {}".format(Total_hours))
    print("-" * 35)
    print("Total number of minutes worked = {}".format(Total_mins))
    print("-" * 35)
    print("Total amount earned = ${:.2f}".format(Total_amount))
    print("-" * 35)
    print("\nThanks for using Time Tracker!❤\n")