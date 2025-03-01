import random

# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"



dice_art = {
    1 : ("┌─────────┐",
         "│         │",
         "│    ●    │",
         "│         │",
         "└─────────┘" ),
    2 : ("┌─────────┐",
         "│ ●       │",
         "│         │",
         "│       ● │",
         "└─────────┘" ),
    3 : ("┌─────────┐",
         "│ ●       │",
         "│    ●    │",
         "│       ● │",
         "└─────────┘" ),
    4 : ("┌─────────┐",
         "│ ●     ● │",
         "│         │",
         "│ ●     ● │",
         "└─────────┘" ),
    5 : ("┌─────────┐",
         "│ ●     ● │",
         "│    ●    │",
         "│ ●     ● │",
         "└─────────┘" ),
    6 : ("┌─────────┐",
         "│ ●     ● │",
         "│ ●     ● │",
         "│ ●     ● │",
         "└─────────┘" )
}


dice = []
total = 0
number_dice = int( input("How many Dice? "))


for die in range(number_dice):
    dice.append(random.randint(1,6))


for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end="")
    print()


for die in dice :
    total += die 
    
    
print(f"Total: {total}")
