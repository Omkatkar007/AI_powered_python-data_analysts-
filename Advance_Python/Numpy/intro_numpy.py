import numpy as np 

# python lists 

l = [1,2,3,4,5]
result = []
for i in l:
    result.append(i*2)

print(result)

# numpy arrays

n = np.array([1,2,3,4,5])
result = n*2 
print(result)

# numpy arrays are mutable

n = np.array([1,2,3,4,5])
b = np.zeros(5)
c = np.ones(5)
d = np.full(5,5)
e = np.arange(5)
f = np.linspace(0,1,5)
g = np.logspace(0,1,5)
h = np.eye(5)
i = np.random.rand(5)
j = np.random.randint(5,size=5)
k = np.random.choice(5,size=5)
l = np.random.permutation(5)
m = np.random.choice(5,size=5,replace=False)                       
print(n)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)

# numpy vectorized functions

zx = np.array([1,2,3,4,5])
result1 = zx + 10
result2 = zx * 10
result3 = zx > 1

print(zx)
print(result1)
print(result2)
print(result3)

# numpy matrix

m = np.array([[1,2,3],[4,5,6],[7,8,9]])
z = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(m,z)

# numpy basic operations

a = np.array([1,2,3,4,5])

a.sum()
a.mean()
a.std()
a.max()
a.min()
a.argmax()
a.argmin()
a.prod()
a.cumsum()
a.cumprod()

# numpy basic operations                        