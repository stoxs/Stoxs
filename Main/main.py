from exportDriver import exportdriver
from tableDriver import tabledriver
from graphDriver import graphdriver



command = input("Enter command: ")
while (command != "quit"):
    if (command == "export"):
        exportdriver()
    elif(command == "table"):
        tabledriver()
    elif (command == "graph"):
        graphdriver()
    elif (command == "help"):
        print("(command list)")
    else:
      print("Invalid input. Enter 'help' for more list of commands.")
    command = input("Enter command: ")



