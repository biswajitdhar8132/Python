print("WELCOME TO MY QUIZ GAME!!")

play = input("You want to play? ")

if play.lower() == "yes":
    print("OKAY! LET'S PLAY.")
    score = 0
   
else:
    quit()

answer = input("What is the capital of INDIA? ")
if answer.lower() == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
answer = input("What is the capital of TRIPURA? ")
if answer.lower() == "agartala":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")

answer = input("What is the capital of UTTAR PRADESH? ")
if answer.lower() == "lucknow":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")

answer = input("What is the capital of RAJASTHAN? ")
if answer.lower() == "jaipur":
    print("Correct!")
    score += 1
    
else:
    print("Incorrect!")

print(f"Yout got {score} out of 4 questions correct!")
print(f"Your score: {(score/4)*100}%")

