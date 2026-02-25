# Tuple is immutable

t = (1, 2, 3)

# single element tuple

t1 = (1,)

# accessing elements

T2 = (1, 2, 3, 4, 5)
print(T2[2])

# slicing

print(T2[1:4])

# Methods

t3 = (1, 3, 4, 6, 8, 1, 1, 1, 4, 4,)

print(len(t3))

print(t3.count(1))

print(t3.index(4))

# to convert list to tuple

tup = (1, 2, 3, 4, 5)
list1 = list(tup)
print(list1)

list1.append(6)

list1.insert(0, 0)
print(list1)
