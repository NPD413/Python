"""the elif is a keyword  in python way of saying if the previous codition were not true ,then try this condition,the elif keyword allows you to check multiple expression for true and executr a block of code as soon as one of the conditions evalutes to true"""
#a=30
#b=60
a,b=map(int,input("enter a,b:").split())
if a>b:
    print("a is greater than b")
elif b>a:
    print("b is greater than a")
"""multiple elif statements
there can be multile condition in order and execute the first one that is true"""
price=5000
if price==9000:
    print("converse shoes")
elif price > 9000:
    print("watch")
elif price <= 104:
    print("mc'd")
elif price == 5000:
    print("savings")
day=3
if day==1:
    print("mon")
elif day==2:
    print("tue")
elif day==3:
    print("wed")
elif day==4:
    print("thu")