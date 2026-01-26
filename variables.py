#variables are created when you assign a value to it it basically a class which contains student identity
"""variable names are case sensitive
variables can be declared through casting as well  CASTING is is to specify the data type of a variable this can be done through casting"""
x=int(15)
y=str("NPD")
z=float(4/10)
print(x,y,z)#prints the values
x = "dharani"
y = "6CBC01"
print(x) #note the to print a variable we must not quote it 
print (y)
print(x,y)
print(("my name is") + x + ("studying in") + y)
print(x,end=" ")
print (y)
#to find the type of the variable we use the type()function
x=15
y="string"
print(type(x))
print(type(y))
#variables are case-sensitive both are A's but they still act different
A="anusha"
a="anusha"
print(A,end=" ")
print(a)
"""variable names can be shaort form such as x,y etc just like an pet name
a variable must start with letter or the underscore character
a variable cannot strat with a number
a varaiable can only consist of alpa numeric and underscore eg(a_z)
variables are case senitive """
#correct variable names
var="dharani"
var1="dharani1"
dee_var="dha"
MYvar=23
#illegal variable names
#2myvar="dha"
#my-var="dee"
"""types of variable names camel case,pascal case,snake case"""
#camel case expect the first letter of the word start with an capital letter"""
myNameIs="NPD"
#pascal case all the first letter of the word start with the capital letter"""
myNameIs="NPD"
#snake case is seprated by an underscore character
my_name_is="NPD"
#assign multiple values
x,y,z="orange","banana","apple"
print(x,y,z)
#assign the same values to each variable
x=y=z="orange"
print(x,y,z)
#if the collection is in list,tuple python allows tp extract the values into variable this is called unpacking
fruits=["apple","orange","lichi"]
x,y,z=fruits
print(x,y,z)
#global variables that are created outside of a function global variables can be used by everyone,both inside of functions and outside
x="overworld"
def myfunc():
    print("python is"+ x)
myfunc()
#create a variable inside a function with the same name as the global variable
x="fab"
def myfunc():
    x="intresting"
    print("python is"+ x)
myfunc()
print("python is"+ x)