#Solution of problem 5

hr = int(input("Enter the hours: "))
mn = int(input("Enter the minutes: "))
ampm = input("AM or PM ? ").upper()

if 5 > hr and ampm == "PM":
    print("GOOD AFTERNOON")
elif  hr >= 5 and ampm == "PM":
    print("GOOD EVENING")
elif hr <= 3 and ampm == "AM":
    print("GOOD NIGHT")
elif hr > 3 and ampm == "AM":
    print("GOOD MORNING")