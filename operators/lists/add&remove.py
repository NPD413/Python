"""append() method is used to add an item to the end of the  list"""
list=["Girls","like","you"]
list.append("run")
print(list)
"""insert() method is used to insert anitem at the specified index"""
list.insert(1,"boys")
print(list)
"""to append elements from another list to the current list,use the extend() method"""
list1=["run",'down',"guys","like","me"]
list2=["Girls","like","you"]
list2.extend(list1)
print(list2)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
"""the extend() method does not have to append list,you can add any iterable object(tuple,sets,dictionaries)"""
list3=["kerala","pune","punjab"]
tuple=("chennai","banglore")
list3.extend(tuple)
print(list3)
"""the remove() method is used to remove specific item from the string"""
var=["let","the","curse","be","true"]
var.remove("true")
print(var)
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)#removes only the first occurance of banana
"""the pop() method removes the specified index"""
thislist.pop(1)
print(thislist)
thislist.pop()#remove the last item from the list
print(thislist)
"""del keyword also removes the specified index"""
city=["banglore","mumbai","chennai"]
del city[1]
print(city)
del city #delete's the entire list
"""clear() is method that empties the entire list"""