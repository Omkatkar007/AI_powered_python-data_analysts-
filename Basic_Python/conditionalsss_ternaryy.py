# conditionals ( if, elif, else) and ternary operator

age = int(input("enter your age: "))

if age < 18:
    print("you are a minor")
else:
    print("you are an adult")

if age % 2 == 0:
    print("your age is even")
else:
    print("your age is odd")

# ternary 
status = "adult" if age >= 18 else "minor"
print(status)