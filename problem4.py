'''4. Write a Python program that prints whether a given year is a leap year or not. 
Take input from the user (e.g. Input 1900 should output “Not a leap year”). '''

yr = int(input("Enter a year: "))
if (yr % 4 == 0 and yr % 100 != 0) or yr % 400 == 0:
    print("It is Leap Year.")
else:
    print("It is Not a Leap Year.")