city=["banglore","chennai","mumbai"]
for x in city:
    print(x)
"""list comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list"""
fruits=["banana","apple","mango","kiwi","lichi","papaya"]
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)
family=["dad","mom","son","daughters"]
newlist=[]
for x in family:
    if "s" in x:
        newlist.append(x)
print(newlist)
fruits=["banana","apple","mango","kiwi","lichi","papaya"]
newlist=[x for x in fruits if x!="apple"]
print(newlist)
fruits=["banana","apple","mango","kiwi","lichi","papaya"]
newlist=[x for x in range(4) if x<4]
print(newlist)
language=["python",'sql',"html","c++","java"]
list=[x.upper() for x in language]
list=[x.islower() for x in language]
list=["go" for x in language]
print(list)
fruits = ['apple', 'banana', 'cherry']
newlist = ['apple' for x in fruits]
print(newlist)