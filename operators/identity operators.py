"""identity operators are used to compare the objects,not if they are equal but if they are actually the same object,with the same memory location"""
"""Is =returns true if both variables are the same object
is not = returns true if both variables are not the same object"""
x=["apple","mango"]
y=["apple","mango"]
z=["kiwi"]
k=x
print(x is y)
print(x is z)
print(x==y)
print(x is k)#is operator  returns true if both the variables point to the same obj
print(x is not y)#returns true is if both the operator  does not points the same variable point and object
print( x is not k)
""" difference between is and ==
is checks the variable point to the same object in the memory
== checks if the values of both variables are equal"""
x=[1,2,3]
y=[1,2,3]
print(x==y)
print(x is y)

