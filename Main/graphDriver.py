def graphdriver ():
    command = input("Enter graph command: ")
    while (command != "back"):
        if (command == "line"):
            print("line graph")
        elif (command == "candlestick"):
            print("candlestick graph")
        elif (command == "help"):
            print("(graph command list)")
        else:
            print("Invalid input. Enter 'help' for more list of commands.")
        command = input("Enter graph command: ")