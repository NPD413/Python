"""dictionaries are used to store data values inkey:value pairs
a dictionary is a collection which is ordered*,changeable and do not allow duplicates"""
dict={
    "bank":"SBI",
    "Manger":"HEAD",
    "client":"NPD"
}
print(dict)
print(dict["bank"])
"""dictionary cannot have the same key twice"""
dict1={
    "bank":"SBI",
    "Manger":"HEAD",
    "client":"NPD"
   # "client":"NPD"
}
print(dict1)
print(len(dict1))
"""the values in an dictionary can be of any data types"""
"""dictionary can contain any data type can contain list,tuple,sets,boolean"""
dict2={
    "brand":"Rolex",
    "year": 1999,
    "model":"datejust"
}
print(dict2)
"""it is possible to use dict() construct to make a dictionary"""
"""thisdict1=dict(name="NPD",year="2004",city="bangalore")
print(thisdict1)"""
