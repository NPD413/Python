print(10 > 9)
print(10 < 9)
print(10 == 9)

a=200
b=150
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
"""evaluate two variables"""
x="hello"
y=20
print(bool(x))
print(bool(y))
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myfun():
   return True
print(myfun())

def myfun():
   return True
if(3>2):
   print("yes")
else:
   print("no")
"""print yes if the function returns true,otherwise print no"""
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
"""check if an object is an integer or not"""
x=150
print(isinstance(x,int))
print(isinstance(x,str))
print(isinstance(x,float))
"""bool is false for 0 and true for 1"""
print(bool(0))
print(bool(1))
print(bool(2))