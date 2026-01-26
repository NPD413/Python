"""there are several to join two or more sets in python
the union() and  update() method joins all the items from both the sets
the intersection() methods keeps only duplicates
the difference() method keeps the items from the first set that are not in the other set(s)
the symmetric_diffrence() methods keeps all items except the duplicates"""
set1={1,2,3,4}
set2={4,5,6,7}
set3=set1.union(set2)
set4=set1.difference(set2)
set5=set1.intersection(set2)
set6=set1.symmetric_difference(set2)# we can use(^) instead of symmetric_diffeerence
set7=set1^set2
print(set7)
print(set6)
print(set4)
print(set5)
print(set3)
"""use the frozenset() constructor to create a frozenset from any iterable"""
x=frozenset({"brain","lungs","heart"})
print(x)
print(type(x))