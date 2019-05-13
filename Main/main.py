from exportDriver import exportdriver
from tableDriver import tabledriver
from graphDriver import graphdriver

# Main driver for the stoxs app: Querying, viewing and graphing data from our local databases

print("+--------------------------------------------------------------------------+\n|                          Welcome to Stoxs v1.0                           |\n|--------------------------------------------------------------------------|\n|                  made by Zayaan Moez and Malcolm Yeh                     |\n|                                                                          |\n|                < Enter 'help' to see list of commands >                  |\n+--------------------------------------------------------------------------+")
command = input("Enter command: ")
while (command != "quit"):
    if (command == "export"):
        exportdriver()
    elif(command == "table"):
        tabledriver()
    elif (command == "graph"):
        graphdriver()
    elif (command == "help"):
        print("Command         Description\n-------         -----------\nexport          export data to .csv\ntable           get data in table\ngraph           graph data\nquit            exit program")
    else:
      print("Invalid input. Enter 'help' for more list of commands.")
    command = input("Enter command: ")



