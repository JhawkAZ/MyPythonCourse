counter=int(input('enter limit '))

while True:
    if counter ==20:
        break
    elif counter%2 != 0:
        print(counter,end=" ")
    counter +=1