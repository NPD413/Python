"""and or not are some of the logical statements which can be used with the if statements python has three logical operators"""
a=200
b=33
c=500
if a>b and c<b:
    print("no")
elif a<b or a>c:
    print("yes")
elif not a<b:
    print("yup")

username="npd"
password=2004
is_verified=True
if username and password and is_verified:
    print("yes")
else:
    print("no")

score=60
if score>0 and score<100:
    print("yes")
else:
    print("no")