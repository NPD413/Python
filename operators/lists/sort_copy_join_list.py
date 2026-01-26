"""list objects have a sort() method that will sort the list alphanumerically,ascending by default"""
country=["india","usa","uae","russia"]
country=[x.upper()for x in country]
country.sort()
print(country)
price=["$400","$500","$35.00","$600","$650.50"]
price.sort()
print(price)
"""to sort descending,use the keyword argument reverse = True"""
price.sort(reverse = True)
print(price)
"""we can use str.lower key function for case sensitive sort"""
country.sort(key = str.lower)
print(country)
"""if we want to reverse the order of the list items"""
country.reverse()
print(country)
"""You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2."""
""" the built-in List method copy() to copy a list."""
sports=["cricket","basketball",'football']
list=sports.copy()
print(sports)
""" use the list() method to copy"""
"""thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)"""
"""we use + operator to join two list"""
list1=["a","b","c"]
list2=[1,2,3]
list3=list1+list2
print(list3)
a=["nlp","ai","mi"]
b=["kick","shrink","wrink"]
for x in b:
    a.append(x)
print(a)
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)