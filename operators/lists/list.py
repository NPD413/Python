"""Lists are used to store multiple items in a single variable"""
""" there are 4 built in data types in python used to store collections of data, list,tuple,set,directory all with different qualities and usage
lists are created using a square brackets"""
list1=["passion","love","intimacy"]
print(list1)
"""list items are ordered,changeable,and allow duplicate values list items are indexed,the first item has index[0],the secound one has the index[1]"""
"""ordered -when we say list is ordered which means items have a definite order,and the order will not change if you had an new item it will be added in the end of the list
changable=we can add,remove,change an item in a list after it has been created
duplicates=since list is been indexed it can have items of the same value"""
li=["apple","banana","apple","banana"]
print(li)
"""the length of the list use the len() function"""
print(len(li))
li1=["dha","brainrot",True,56]
print(type(list))#lists are defined as objects with the data type 'list'
"""it's poosiple to create a list with the list constructor"""
list1=list(("me","you",3))
print(list1)
print(type(list1))
print(list1[0])