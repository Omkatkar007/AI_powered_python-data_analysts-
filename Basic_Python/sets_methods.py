# stores multiple items in a single variable which is unordered and unIndex
mset = {"apple", "banana", "cherry"}
print(mset)

# empty set format

set1 = set()

# methods

set2 = {"apple", "banana", 1, 2, "om"}
set2.add("katkar")
print(set2)

set2.update(["mango"])
print(set2)

set2.remove("banana")
print(set2)

set2.discard("katkaraaa")
print(set2)

set2.pop()

a = set2.pop()
print(a)
print(set2)

set2.clear()
print(set2)

# operations

set3 = {1, 2, 4}
set4 = {2, 3, 4}
result = set3.union(set4)
print(result)

result1 = set3.intersection(set4)
print(result1)

result2 = set3.difference(set4)
print(result2)


