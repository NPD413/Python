"""you can axcess the items of the dictionary by refering to its key name,inside square bracket"""
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x=dict["model"]
print(x)
"""also get() that will give you the same result:"""
y=dict.get("year")
print(y)