"""you can axcess the items of the dictionary by refering to its key name,inside square bracket"""
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x=dict["model"]
z=dict.keys()#the list of the keys is view of the dictionary 
print(z)
print(x)
"""also get() that will give you the same result:"""
y=dict.get("year")
print(y)

var={
    "college":"pu",
    "year": 2023,
    "course":"cse"

}
x=var["year"]=2027
print(var)
"""the values() method will return a list of all the values in the dictionary"""
x=var.values()
print(x)
w=var.items()#the item() eill return each item in a dictionary as an tuple in a list
print(w)
mine={
    "name":"xxx",
    "need":"yyy",
    'color':"black"
}
if "need" in mine:
    print("yes I do!")
else:
    print("NAH!")
"""we cxan use the update() method to update the dictionary with the items from the given argument."""
var.update({"name":"zzz"})
print(var)
"""to add we use nameof the dict["the key to be changed"]:['the new value']
and also we can use update() method"""
mine["model"]="yellow"
print(mine)
"""remove dictionary items we use pop() method"""
shoe={
    "brand":'converse',
    "style":"converse-chunk",
    "origin":"germany",
    "color":"black"
}
shoe.pop("color")
print(shoe)
"""popitem is used remove the last inserted item """
shoe.popitem()
print(shoe)
"""the del keyword removes the item with the specified"""
del shoe["brand"]
print(shoe)
"""to copy a dict"""
v=shoe.copy()
print(v)

family={
"child1":{
    "name":"NPD",
    "year":2004,
},
"child2":{
    "name":"NPB",
    "year":2007
},
"child3":{
    "name":"NSD",
    "year":2007
}
}

