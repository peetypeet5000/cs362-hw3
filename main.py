#Leap Year Checker:
#Run with python3 main.py [year]
#where [year] is a valid integer.

import sys


#Takes string input and checks if it is a leap year
# Input - String that is an integer
# Output - Prints to stdout if year is leap or not
def isLeapYear(input):

    year = int(input)

    # Check if leap year
    if(year % 4 == 0):
        if(year % 100 == 0 and year % 400 != 0):
            print(year, "is not a leap year!")
        else:
            print(year, "is a leap year!")
    else:
        print(year, "is not a leap year!")




# Driver code
isLeapYear(sys.argv[1])


