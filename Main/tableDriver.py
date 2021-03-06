from get_df import *

def tabledriver ():
    command = input("Enter table command: ")
    while (command != "back"):
        if (command == "all"):
            company, market = input("Enter Company Symbol and Market Name: ").split()
            df = getcompanytable(company, market, '2019-04-01', '2019-05-08')
            print(df)
        elif (command == "range"):
            company, market, start, end = input("Enter Company Symbol, Market Name, Start Date and End Date: ").split()
            df = getcompanytable(company, market, start, end)
            print(df)
        elif (command == "help"):
            print("Multiple inputs must be space separated.\nCommand         Description\n-------         -----------\nall             display data for all dates\nrange           display data for given range of dates\nback            return to main menu")
        else:
            print("Invalid input. Enter 'help' for more list of commands.")
        command = input("Enter table command: ")
