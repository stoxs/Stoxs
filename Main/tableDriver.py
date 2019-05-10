from get_df import *

def tabledriver ():
    command = input("Enter table command: ")
    while (command != "back"):
        if (command == "all"):
            company, market = input("Enter Company Symbol and Market Name: ").split()
            getcompanytable(company, market, '2019-04-01', '2019-05-08')
        elif (command == "range"):
            company, market, start, end = input("Enter Company Symbol, Market Name, Start Date and End Date: ").split()
            getcompanytable(company, market, start, end)
        elif (command == "help"):
            print("(table command list)")
        else:
            print("Invalid input. Enter 'help' for more list of commands.")
        command = input("Enter table command: ")