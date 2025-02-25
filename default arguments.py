# Default argument = a default value for certin parameters
#                  = Default is used when that argument is omitted
#                  = make your function more flexible ,reduce # from arguments
#                  = 1. positional, 2. Default 3. keyword, 4. arbirary

# -------------Defualts arguments---------------------

def net_price (list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)


print(net_price(500))
print(net_price(500 , 0.05 , 0))
print (net_price(500,0.07,0.1))


#------------- keyword arguments ---------------------


def get_bumber (country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

Phone_number = get_bumber(country= +92, area=300, first=664,last=8871)

print(Phone_number)


#-------------ARBITRARY arguments----------------------


def exaample (*args):
    total = 0
    for agr in args:
        total += agr
    return total

print(exaample (1,44))





def display_name (*agrs):
    for agr in agrs:
        print(agr,end=" ")
    print()

display_name("Anas", "Sultan","Tipu")



def print_address(**kwargs):
    for  value in kwargs.values():
        print(f" {value}")

print_address(name="Anas",Last_bane= "Sultan",Street="#192",city="Faisalabad")



def Full_address (*abc,**cba):
    for a in abc :
        print (a, end=" ")
    print()

    if "art" in cba :
        print (f"{cba.get('street')} {cba.get('aprt')}")
    elif "pobox" in cba:
        print(f"{cba.get('street')}")
        print(f"{cba.get('pobox')}")

    else:
        print(f"{cba.get('province')} {cba.get('city')}")

Full_address("Mr.", "Tipu","Sultan",
             street = "Street #194",
             city = "Faisalabad",
             province = "Punjab",
             pobox = "Po box #1954",
             aprt = "100")


