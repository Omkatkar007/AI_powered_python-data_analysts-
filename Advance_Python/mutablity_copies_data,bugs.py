# mutablity 

a = [1,2,3]
b = a
b[0] = 4
print(a)
print(b)     # both changes because both a and b point to the same list object in memory

# copies data

a = [1,2,3,4]
b = a.copy()

b[0] = 5
print(b)
print(a)     # a is unchanged because b is a copy of a, not a reference to the same list object

# dicts

d = {'a':1,'b':2}
e = d.copy()
e['a'] = 5
print(d)
print(e)

# hidden mutataion inside functions

def add_items(items):
    items.append(4)

z = [1,2,3]
add_items(z)
print(z)

# mutable types

class A:
    def __init__(self,x):
        self.x = x
    def __str__(self):
        return str(self.x)
    def __repr__(self):
        return str(self.x)

a = A(1)
b = a
b.x = 2
print(a)
print(b)

# mutable types

class A:
    def __init__(self,x):
        self.x = x
    def __str__(self):
        return str(self.x)
    def __repr__(self):
        return str(self.x)