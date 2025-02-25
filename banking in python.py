def show_balance (balance):
    print(f"Your Balnce is Rs.{balance}")

def deposit ():
    amount = float(input("Enter the number to Deposited: "))

    if amount < 0 :
        print("that's not a valid number to deposit")
        return 0
    else:
        return amount
    
def withdraw (balance):
    amount = float(input("Enter the number to Withdrawn: "))

    if amount > balance :
        print("Insufficient balance")
        return 0
    elif amount < balance:
        return amount


def main ():    
    balance = 0
    is_running = True

    while is_running :
        print("Welcome to the Bank")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exite:")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_balance(balance)

        elif choice == "2":
            balance += deposit()

        elif choice == "3":
            balance -= withdraw(balance)
        
        elif choice == "4":
            is_running = False

        else:
            print("That's not a valid Choice")


    print("it's been a grate pleaure to have you: ")

if __name__ == "__main__":
    main()