"""assignment opearators are used to assign values to variables"""
x=int(5)
x+=5#x=x+5
x-=5#x=x-5
x*=5#x=x*5
x/=3#x=x/5
x//=5
x%=5
x**=5
#x &= 3
#x|=3
#x^=3
print(x)
numbers=[1,2,3,4,5]
count=len(numbers)
if count>3:
    print(f"list has more {count} elements")
if(count:=len(numbers))>3:
    print(f"the list more {count} elements")
numbers=[1,2,3,4,5,6]
if(count:=len(numbers))<3:
    print(f"the list has {count} elements")
else:
    print(f"the list has {count} elements more")