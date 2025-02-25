# Python slot machine

import random

def spin_row ():
    symboles = ["❤️","💕","😘","😍","😒","👌"]

    return[random.choice(symboles) for _ in range (3)]

def print_row (row):
    print()
    print(" | ".join(row))
    print()


def get_payout (row,bet):
    if row [0]==row [1] == row[2]:
        if row[0] == '💕':
            return bet * 35
        elif row[0] == '❤️':
            return bet * 30
        elif row [0] == '😘':
            return bet * 25
        elif row [0] == '😍':
            return bet * 20
        elif row[0] == '👌':
            return bet * 15
        elif row [0] == '😒':
            return bet * 10
        else:
            return 0
    return 0


def main ():
    balance = 100
    print("Welcome to the Python slot machine")
    print("Symboles : 👌😒😍😘💕❤️")


    while balance > 0 :
        print(f"Your Balance is Rs.{balance}")

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print ("Invalid Amount: ")
            continue

        bet = int(bet)

        if bet > balance:
            print("Inficent Balance: ")
            continue

        if bet < 0 :
            print("The must be in garter then 0")
            continue

        balance -= bet

        row = spin_row()
        print ("spinning...")

        payout = get_payout (row , bet)

        if payout > 0 :
            print (f"you won Rs.{payout}")

        else:
            print("Better luck next time: ")

        balance += payout

        play_again = input("Do you want to play again (Y/N): ").lower()

        if play_again == "n":
            break

    print (f"Thanks for playong with us your ramining balance is {balance} ")



if __name__ == '__main__':
    main()