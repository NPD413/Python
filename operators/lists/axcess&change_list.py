"""list items can be axcessed and you can axcess them by referring to the index number"""
ls=[1,2,"me"]
print(ls[1])
print(ls[1:])
list=["roll","biryani","friedrice","trufflecake"]
print(list[2 :])
print(list[-3])
print(list[2:5])
print(list[:3])
"""to chefck if the items exists to detrmine"""
list=["roll","biryani","friedrice","trufflecake"]
if "cake"in list:
    print("is not in list")

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
mylist = ['apple', 'banana', 'cherry', 'orange', 'kiwi']
print(mylist[1:4])
"""change items in the list  to change the value of a specific item,refer to the index number"""
list=["pizza","roll","cake","cola"]
list[1]="ice-cream"
print(list)
list[1:3]=["ice","burger"]
print(list)
"""if u want to insert use the insert() method to insert item at an specified index"""
list.insert(2,"polarbear")
print(list)
mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist)