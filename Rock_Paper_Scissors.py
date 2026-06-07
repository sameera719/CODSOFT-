import random
user_score = 0
computer_score = 0
while True:
    print("\n -----ROCK_PAPER_SCISSORS GAME-----")
    user = input("Rock, Paper or Scissors: ").lower()
    if user != "rock" and user != "paper" and user != "scissors":
        print("Invalid Choice")
        continue
    computer = random.choice(["rock", "paper", "scissors"])
    print("User:",user)
    print("Computer:", computer)

    if user == computer:
        print("Match is Tie")

    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        print("You Win")
        user_score += 1

    else:
        print("Computer Wins")
        computer_score +=1
    print("User Score:", user_score)
    print("Computer Score:", computer_score)

    play_again = input("Play Again? (yes/no): ").lower()

    if play_again == "no":
        break

print("Game Over")
