food = input("What is your favorite food? ")
if (food =="pizza"):
    print("Pizza is my favorite")
elif (food == "tacos"):
    print("Tacos is my 2nd favorite")
else:
    print("You like " + food +"? I might like it too.")

favorite_month =input("What is your favorite month? ")
month = favorite_month

if month=='1' or month=='2' or month=='3':
    likeable_meter='Way too Cold'
elif month==4 or month==5 or month==6:
    likeable_meter='Now this is a good time of the year'
elif month=='7' or month=='8' or month=='9':
    likeable_meter='Way Too hot'
elif month=='10' or month=='11' or month=='12':
    likeable_meter="If it weren't for Thanksgiving and Christmas it would be a bit too cold"
else:
    likeable_meter='Do not know that month'
print(likeable_meter)