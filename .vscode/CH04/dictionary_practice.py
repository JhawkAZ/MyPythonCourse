squares={1:1,5:25,2:4,3:9,4:16}
print(squares)

for key,value in squares.items():
    print(f"The square of {key} is {value}")

print('pop(4)=',squares.pop(4))
print('squares',squares)
squares[6] = 36
print('squares added [6]: ',squares)

print('squares.popitem() returns ',squares.popitem())
print('squares after popitem',squares)

del squares[2]
print('squares after del squares[2]',squares)
#del squares[7] throws error
squares.clear()
print('squares after squares.clear()',squares)
del squares
#print(squares) printing deleted dictionary throws error

values={}
for x in range(1,11,1):
     values[x]=x*3
for x,y in values.items():
  print(f"The value of {x} * 3 is {y}")

values={}
for x in range(1,11):
     values[x]=x*3
for x,y in values.items():
  print(f"The value of {x} * 3 is {y}")
