keep_looping=True

while keep_looping:
    month= int(input("Enter a month numerically: "))
    day =int(input("Enter a day numerically: ")) 

    if (month> 0 and month <13 and day > 0 and day<=31):
        keep_looping = False
    else:
        print('Invalid entries. enter 1-12 for monht, enter 1-31 for days')
print('You did it')