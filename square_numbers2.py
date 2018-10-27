# **************************************************
# *   Printing out the first n square numbers      *
# *   These arguments are passed from Command Line *
# *   into the program                             *
# **************************************************

import sys             # COMMAND LINE ARGUMENTS:
                       #   In the command line, we can start a program 
                       #   with additional arguments.
                       #   'sys' module: an additional module of the Python,
                       #   that manages all Arguments in command line. 

Max = int(sys.argv[1]) # sys.argv[1] is the second Argument in command line.
                       # set how many items the list have (List Length).

myList = []            # set an empty List: 'myList'


for x in range(1, Max+1):
    n = x**2
    myList.append(str(n))        # Add an item to the end of the list; 
                                 #  (item previously converted from integer to string)

myString = ", ".join(myList)     # concatenation of the strings in the List: 'myList'
print(myString)


