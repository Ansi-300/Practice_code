import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

rows = 3
columns = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}


symbol_values = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}
def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break  
        else:
            winnings += values[symbol] * bet 
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row])

        print()

def deposit():
    while True:
        amount = input("Enter the amount to deposit: ")

        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be grater then zero 0: ")

        else:
            print("plz Enter a number: ")

    return amount

def get_number_of_lines ():
    while True:
        lines = input("Enter a number of line to bet on (1- " + str(MAX_LINE) + ")? ")

        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter a valid number of line ")

        else:
            print("plz Enter a number of Line: ")

    return lines

def get_bet ():
    while True:
        amount = input("Would you like bet each line ")

        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"amount must be {MAX_BET} - {MIN_BET}")

        else:
            print("plz Enter a number: ")

    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough amount to bet on your current balance is {balance}: ")

        else:
            break

    print(f"Your are betting on {bet} on {lines} Lines. Total bet is equal to {total_bet}")

    slot = get_slot_machine_spin(rows , columns,symbol_count)
    print_slot_machine(slot)
    winnings ,winning_lines = check_winning (slot, lines,bet , symbol_values)
    print(f"You won {winnings}.")
    print(f"You won on Lines:", *winning_lines)
    return winnings - total_bet


def main ():
    balance = deposit()
    while balance > 0:
        print(f"Your current balance is {balance}")
        answer = input ("Press enter to spin (Q) to Quit ").lower().strip()
        if answer == "q":
            break
        else:
            balance += spin(balance)
            

        if balance <= 0:
            print("You ran out monay! Game Over!")
    print(f"You left with {balance}")
        
    
main()
