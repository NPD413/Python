set={"mac","hp",'lenovo',"del"}
set.add("samsung")
print(set)
"""to join two sets we use the update() method"""
set1={"green","orange","blue","indigo"}
set2={'violet',"pink","red","maroon"}
set1.update(set2)
print(set1)
"""use remove() method """
family={"mom","dad","child1","child2","child3"}
family.remove("child3")
family.discard("child2")#can beremoved using the discard function as well
print(family)
"""del,clear are used to remove the entire set"""
