# write 
a = ("demo testing")
file = open("file.txt","w")
file.write(a)
file.close()

# read

file =  open("file.txt","r")
content = file.read()   # for reading line use content = file.readlines()
print(content)
file.close()

# append 
p = "/n appending data"
file = open("file.txt","a")
file.write(p)
file.close()

# with

n = "/n using with"
with open("file.txt",'a')as file:
    file.write(n)