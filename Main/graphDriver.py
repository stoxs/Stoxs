from graph import *

def graphdriver ():
    command = input("Enter graph command: ")
    while (command != "back"):
        if (command == "price"):
            company, market = input("Enter Company and Market Name: ").split()
            plot_price(company, market)
        elif (command == "perchg"):
            company, market = input("Enter Company and Market Name: ").split()
            plot_perchg(company, market)
        elif (command == "netchg"):
            company, market = input("Enter Company and Market Name: ").split()
            plot_netchg(company, market)
        elif (command == "volume"):
            company, market = input("Enter Company and Market Name: ").split()
            plot_volume(company, market)
        elif (command == "help"):
            print("Multiple inputs must be space separated.\nCommand         Description\n-------         -----------\nprice           opening and closing prices over time\nperchg          percent change over time\nnetchg          net change over time\nvolume          volume over time")   
        else:
            print("Invalid input. Enter 'help' for more list of commands.")
        command = input("Enter graph command: ")
