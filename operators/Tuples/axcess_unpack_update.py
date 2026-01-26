tup=("Digital","assert","scam")
print(tup[1])
print(tup[-1])
print(tup[1:3])
print(tup[:2])
print(tup[2:])
if "assert" in tup:
    print("yes")
else:
    print("no")
""" tuples are unchangeable,meaning that you cannot change,add, or remove items once the tuple is created"""
"""but we can convert the tuple into a list ,and convert the list back to tuple"""
x=("news","sports","cartoon")
y=list(x)
y.append("movies")
y[3]="entertainment"
y.remove("news")
x=tuple(y)
print(x)
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
games=("badmintton","chess","carrom","monopoly","volleyball")
(outdoor,*indoor)=games
print(outdoor)
print(indoor)
"""join two tuple"""
tuple1=("pink","yellow","green")
tuple2=("blue","white","black")
tuple3=tuple1+tuple2
print(x)
print(tuple3)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)
tuple1=("pink","yellow","green")
y=tuple1.index("yellow")
print(y)