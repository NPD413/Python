"""the else keyword catches anything which isn't caught by the preceeding conditions.the else statement the else condition is exectuted when the if condition and else condition returns false"""
a=500
b=600
if a==b:
    print("a is equal to be")
elif a>b:
    print("a is greater than b")
else:
    print("a is less than b")
"""the else statement provides a default action when none of the previous conditions are true think of it as a "catch-all scenario not covered by your if and elif statements
else statement should come as the last ,elif cannot come after else"""
num=3
if num%2==0:
    print("is an even number")
else:
    print("it is an odd number")
tem=30
if tem<30:
    print("high")
elif tem==0:
    print("freezing")
elif tem>30:
    print("warm")
else:
    print("normal")
username=""
if len(username)>0:
    print(f"welcome,{username}")
else:
    print("invalid{username}")
"""shorthand of using if statements"""
a=5
b=2
#if a<b: print("a is greater than b")
print("a") if a>b else print("b")
a=5
b=5
print("a") if a>b else print("=") if a==b else print("equals")
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)