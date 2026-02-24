# Arithmetic operators
a = 4
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Comparison operators
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# Assignment operators
a += 10
b -= 2
a *= 4

# Logical operators
print((a > b) and (a < b))
print((a > b) or (a < b))
print(not (a < b))

# Membership operators
fruits = ["apple", 3, "xyz"]
print("apple" in fruits)
print("python" not in fruits)

# Identity operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x == y)  # checks only value
print(x is y)  # checks objects memory location
print(x is z)

# Precedence (BODMAS)
# Default
2 + 3 * 4  # 2 + 12
# Forced
(2 + 3) * 4  # 5 * 4


