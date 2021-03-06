#Leap Year Checker:
#Run with python3 main.py [year]
#where [year] is a valid integer.

import sys


#Takes string input and checks if it is a leap year
# Input - String that is an integer
# Output - Prints to stdout if year is leap or not
def isLeapYear(input):
    valid = True

    # See if user entered an integer
    try:
        year = int(input)
    except ValueError:
        print("Please enter a valid integer")
        valid = False

    # Check if leap year
    if(valid):
        if(year % 4 == 0):
            if(year % 100 == 0 and year % 400 != 0 and valid):
                print(year, "is not a leap year!")
            else:
                print(year, "is a leap year!")
        else:
            print(year, "is not a leap year!")




# Driver code, checks arg counts
if(len(sys.argv) == 2):
    isLeapYear(sys.argv[1])
else:
    print("Usage: main.py [year]")


