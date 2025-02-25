import random

low = 1 
high = 100

anaswer = random.randint(low,high)

guesses = 0

is_running = True

print("Welcome to the Pyrhon Game! ")
print(f"Plz Select Between {low} to {high}")

while is_running :
    guess = input("Plz Enter Your Guess! ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1


        if guess < low or guess > high:
            print("The number is out of range: ")
            print(f"Plz Select Between {low} to {high}")
        elif guess < anaswer:
            print("To low! Try agian: ")
        elif guess > anaswer:
            print("To high! Try Again: ")
        else:
            print(f"Correct! The number was {anaswer}")
            print(f"Number of guesses is {guesses}")
            is_running = False

    else:
        print("Invalid guess!")
        print(f"Plz Select number Between {low} to {high}")
