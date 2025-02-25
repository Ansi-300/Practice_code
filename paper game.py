import random

option = ("rock", "paper", "scissor")
running = True
while running:
    player = None
    computer = random.choice(option)

    while player not in option:
        player = input ("Enter Between (rock, paper, scissor)")

    print(f"player {player}")
    print (f"compuer {computer}")

    if player == computer:
        print("its a tie! ")

    elif player == "rock" and computer == "scissor":
        print("You Win! ")
    elif player == "paper" and computer== "rock":
        print("You Win! ")
    elif player == "scissor" and computer == "paper":
        print("You Win! ")
    else:
        print("You Lose")

    play_agin = input("plau agin! (y/n)").lower()
    if not play_agin == "y":
        running = False

print("Thanks For playing!(^_^)")


