list_s = [1, 2, "om", "banana"]
print(list_s)
print(type(list_s))
print(list_s[3])
print(list_s[0:2])


# methods
list = [1, 2, "car", "mob"]
print(len(list))
list.append("bike")
list.insert(3, "clock")
list.extend(["Lamborghini", "no element"])
list.remove("car")
list.pop()
list.pop(3)
print(list.index("bike"))
print(list.count(2))

numbers = [99, 66, 33, 32, 11, 4, 2, 1]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

numbers.clear()

print(numbers)


