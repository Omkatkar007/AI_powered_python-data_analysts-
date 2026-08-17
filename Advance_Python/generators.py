def complex_calc(i):
    return i*i
def num():
    for i in range(10):
       yield complex_calc(i)
a = num()
print(next(a))
print(next(a))  
