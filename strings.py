"""strings in python are surrounded or indicated usually by("")or('')"""
a="NPD"
b='NPD'
print(a,b)
"""we can also quote inside a string,as long as the strings quote does not match"""
dha=("HEY THIS IS ME ,'DHARANI'")
print(dha)
"""multiline string can assign a multipline string to a variable to a variable by using three quotes"""
m="""one of the fascinating mating is kola bear"""
print(m)
"""python does not have any chararcter daatatype,a single character is simply a string with the length of 1"""
a="hey,it's me"
print(a[1])
print(a[0])
print(a[6])
"""the len() function is used to find the length of a string"""
y="let's go on a date" # it counts the space as well
print(len(y))
z="me"
print(len(z))
"""to check if certain phrase or character exist in a string we use (in) keyword"""
txt="you are the best thing that I have ever found"
print("best" in txt)
"""to check if a certain phrase or character does not exist in a string we use a not keyword"""
txt="you are the best thing that I have ever found"
print("not the bestis the truth" not in txt)
x="love"
#print(x[4])#the count starts with 0
""" SLICING- you can return range of characters by using the slice syntax
specify the start index and the end index,seperated by a colon,to return a part of the string"""
kol="BYE,WORLD"
print(kol[2:8])# it will print 2 but not the last 8 
print(kol[0:8])
print(kol[3:6])
"""slice from the start by leaving out the start index,the range will start at the first character"""
b="bye,world"
print(b[:5])#it will get the characters from start to the position specified
print(b[:6])
"""slice to the end by leaving out the end index"""
print(b[3:])
print(b[4:])
print(b[6:])
"""negative indexing use negative indexes to start the slice from the end of the string"""
a="tryme"
print(a[-5:-2])
"""python has a set of built-in-methods that can be used on strings"""
"""the upper() method returns the string in upper case"""
a="dharani"
print(a.upper())#returns the string in upper case
"""the lower() method returns the string in lower case"""
b="me"
print(b.lower())
"""whitespace is the space before/or after the actual text,and very often you want to remove this space"""
a="   watch,me watching you!"
print(a.strip())
"""the replace() method replaces a string with another string"""
c="it's me"
print(c.strip())
"""the replace() method is used to replace a string with another string"""
a="hey this is NPD"
print(a.replace("NPD","dharani"))
"""the split()method splits the string into substrings if it finds instances of the separator"""
c="calm,weird"
print(c.split(","))
print(c.split(":"))
print(c.split("d"))
""" THE METHODS IN STRING ARE
.upper()
.lower()
.split()
.replace()
.strip()"""
"""STRING CONCATENATION to concatenate or combine,two strings you can use the + operator"""
a = "bye"
b = "My world"
c = a + b
print(c)
c=a+" "+b# this will add the space bet two string concatenation
print(c)
a="let"
b="the"
c="evil sprit win"
d = (a+" "+b+" "+c)
print(d)
"""String format as we learned in python ,we cannot combine strings and number like this"""
"""age=21
txt="my name is dharani,I am"+age
print(txt)""" #this will result in error
""" therefore to combine strings and numbers we use f-string or the format() method"""
age = 21
txt = f"my name is dharani I am {age}"#to specify an f string simply put an f in front of the string literal,and add curly brackets{} as placeholders for variables and other operations
print(txt)
price = 34
txt = f"the price is {price} in dollars"
print(txt)
"""a modifier is included by adding a colon : followed by a legal formatting type,like .2f which means fixed point number with 2 pecimal"""
txt2 = f"the price is {price:.2f} dollars"
print(txt2)
txt3 = f"the price is {50*24} dollars"
print(txt3)
"""escape character to insert characters that are illegal in a string use an escape character 
an escape character is a backlash \ followed by the character you want to insert"""
 #var = "we are the so-called "humans" from the space "
var =" we are the so called \"humans\" from the space"
print(var)
a = "BYE\tWORLD!"
print(a)
a = "\110\123\144\132"
print(a)
c="bye!\bworld"
print(c)
d="new\nline"
print(d)
f="hellO World"
print(f.capitalize()) #used to capitalize the first letter
print(f.casefold()) #converts string into lower case
#print(f.center()) #reterns a centered string
x=f.count("o")
print(x)
print(f.count("o"))
print(f.encode())
print(f.endswith("d"))
print(f.find("h"))
print(f.format("hello"))
print(f.title())
""