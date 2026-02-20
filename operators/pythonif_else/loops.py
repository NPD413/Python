"""python has two primitive loop commands:
while loops
for loops
with the while loop we can execute a set of statements as as a condition is true."""
i=1
while i<6:
    i=i+1
    print(i)



a=1
while a<6:
    print(a)
    if(a == 3):
        break
    a+=1
"""continue statement we can stop the current iteration,and continue with the next:"""
"""b=0
while b<6:
    i+=1
    if i==3:
        continue
    print(i)"""
"""with the else statements we run a block of code once when the codition no longer is true"""
i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")
 
 
    