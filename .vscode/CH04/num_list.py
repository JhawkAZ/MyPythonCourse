some_nums=[2,6,4,2,22,54,12,8,-1]
print(len(some_nums))
print('The sum of the list is: ',sum(some_nums))
print(some_nums[2])
y=some_nums[0]
for x in some_nums:
    if x > y:
        y=x
print('the highest number is ',y)

for x in range(len(some_nums) -1):
    print(x)
    if (x%2==0):
        some_nums[x]=11
print(some_nums)
