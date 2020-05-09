#for loop always to be use by iterator
L = [1,2,3,4,5]
T = (1,2,3,4,5)
S = ([1,2,3,4,5])

print ("遍历list")
for x in L:
    print (x)

print("遍历tuple")
for x in T:
    print (x)

print("遍历set")
for x in S:
    print (x)

x = 1
s = 0
while x <=100:
    s +=x
    x +=1

print (s)