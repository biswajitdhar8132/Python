#Solution of problem 6
import random
your_score = 0
comp_score = 0
tie_score = 0

rounds = int(input("How many rounds would you like to play? "))

choices = ["rock", "paper", "scissors"]

for round_number in range(1, rounds + 1):
    print(f"\nRound {round_number} of {rounds}")

    while True:
        your_choice = input("Enter rock, paper, or scissors: ").lower()
        if your_choice in choices:
            break            
        print("Invalid choice, try again.")


    comp_choice = random.choice(choices)
    print(f"Computer chose {comp_choice}.")

    if your_choice == comp_choice: 
        print("→ It's a tie!")
        tie_score += 1
    elif (
        (your_choice == "rock"     and comp_choice == "scissors") or
        (your_choice == "scissors" and comp_choice == "paper")    or
        (your_choice == "paper"    and comp_choice == "rock")):
        print("→ You win this round!")
        your_score += 1
    else:
        print("→ Computer wins this round!")
        comp_score += 1

print("\n=== Game Over ===")
print("You won     : ",your_score)
print("Computer won: ",comp_score)
print("Ties        : ",tie_score)