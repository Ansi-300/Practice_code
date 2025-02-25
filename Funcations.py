# Functions = A block of reusable  in code

#           = place () after the Function name to invoke it
"""def happy_birtday (name,age):
    print(f"HAPPY BIRTHDAY {name}")
    print (f"You are {age} year old!")
    print(f"HAPPY BIRTHDAY TO YOU!")


happy_birtday("Anas",27)




def display_invoice (User_name,amount,Due_date):

    print(f"Hello {User_name}")
    print(f"You have Rs.{amount} outstanding to pay! ")
    print(f"You have to pay before {Due_date}")

display_invoice("Anas",2000, "31 march")"""


# Return statement is used for end an function

# and send back to caller


def add(x,y):
    z = x + y
    return z


def subtract (x,y):
    z = x + y 
    return z

def multiply (x,y):
    z = x * y 
    return z

def divide (x,y):
    z = x / y 
    return z 



print (add(45,78))
print(subtract(789,456))
print (multiply(123,45))
print (divide(789,9))



def user_name (first,last):
    first =first.upper()
    last = last.upper()
    return first  + last


full_name = user_name ("anas","sultan") 

print(user_name)