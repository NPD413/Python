"""condition to check the traffic signal using if-else condition"""
color=(input("color: "))
if(color=="red"):
    print("stop")
elif(color=="orange"):
    print("wait")
elif(color=="green"):
    print("go")
else:
    print("invalid")

    """condition to check the grades of an student"""
    marks=int(input("marks: "))
    if(marks>=90):
        print("A+")
    elif(marks>=80 and marks<90):
        print("B+")
    elif(marks>=70 and marks<80):
        print("c")
    else:
        print("F")
"""to check even or odd"""
num=int(input("num:"))
if(num%2==0):
    print("num is even")
else:
    print("num is odd") 
p=float(input("p: "))
t=float(input("t: "))
r=float(input("r: "))
si=(p*t*r)/100
print(si)
"""to print the sum of 2 numbers """
a=int(input("a: "))
b=int(input("b: "))
sum=a+b
print(sum)
"""to print the area of a square"""
area=int(input("area: "))
sq=area*area
print(sq)
"""to cal average of 2 numbers"""
a=float(input("a: "))
b=float(input("b: "))
sum=(a+b)/2
print(sum)
"wap to input 2 numbers a,b print true if a is greater than b else3 false"
a=int(input("a: "))
b=int(input("b: "))
if(a>=b):
    print("True")
else:
    print("False")
"""to str to int"""
a=int("3")
b=4
print(a+b)