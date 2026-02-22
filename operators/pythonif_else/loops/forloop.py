"""a for loop is used for iterating ovver a sequence(that is either a list,a tuple,a directory,a set,or a string)"""
fruits=["apple","banana","cheery"]
for x in fruits:
    print(x)

for y in "apple":
    print(y)

"""with the break statement we can stop the loop before it has looped through all the items:"""
car=["shift","bes23","ferrari"]
for i in car:
    print(i)
    if i=="bes23":
        break
"""break the statement before the if condition"""
for i in car:
    if i=="bes23":
        break
    print(i)

for i in range(6):
    print(i)

"""the range() function returns a sequence of numbers,starting from 0 by default,and increment by 1 and ends at a apecified number."""
#while i in range(6):
#print(i)
for x in range(2,6):
    print(x)

for y in range(2,30,3):
    print(y)#it increments by 3 as an parameter

for z in range(6):
    print(z)
else:
    print("finally finished")#the else block will not be exedcuted if the break statement is been introduced

for u in range(6):
    if u==3:break
    print(u)
else:
    print("no")
#nested loop will be executed one time for each iteration of the outer loop
adj=["red","blue","tasty"]
fruits=["apple","banana","cheery"]
for x in adj:
    for y in fruits:
        print(x,y)

"""for loop cannot be empty but if you for some reason have a loop with no content put in the pass statement to avoid getting an error"""
