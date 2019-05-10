from get_df import *


def exportdriver ():
    command = input("Enter export command: ")
    while (command != "back"):
        if (command == "all"):
            company, market = input("Enter Company Symbol and Market Name: ").split()
            export_csv(company, market, '2019-04-01', '2019-05-08')
        elif (command == "range"):
            company, market, start, end = input("Enter Company Symbol, Market Name, Start Date and End Date: ").split()
            export_csv(company, market, start, end)
        elif (command == "help"):
            print("(export command list)")
        else:
            print("Invalid input. Enter 'help' for more list of commands.")
        command = input("Enter export command: ")

