# resuable code blocks 

def calculate_tax(revenue,tax_rate=0.08):
    tax_amount = revenue * tax_rate
    return tax_amount

q1_tax = calculate_tax(50000)
q2_tax = calculate_tax(75000,tax_rate=0.10)

print(q1_tax,q2_tax)

# parameter and argument

def greet(name):
    print(name)                 # parameter = name argument = harry 

greet("harry")


# lambda 

add = lambda a,b: a+b
print(add(3,4))