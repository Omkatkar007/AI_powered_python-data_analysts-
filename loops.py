#loops  (for)

items = ['apple','banana','mango']
for items in items:
    print(items)

# with range 

for i in range (0,10):
    print(i)

# wiht difference

for i in range (0,9,2):
    print(i)



# while loop  (runs until the condition becames false)

memory_use = 0
limit_mb = 100

while memory_use < limit_mb:
    memory_use += 25
    print(f"curent memory remaining {memory_use}MB")
print('memory limit reached')


#  break contiune 

for i in range(10):
    if i == 5:
        break
    print(i)


for i in range(5):
    if i == 2:
        continue
    print(i)


# nested 

for i in range(3):              
    for j in range(2):
        print(i,j)


# looping with else 

for i in range(3):
    print(i)
else:
    print("Loop finished")