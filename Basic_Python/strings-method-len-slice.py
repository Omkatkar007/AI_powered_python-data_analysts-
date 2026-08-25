# Multi line string
multi = ''' this is a 
multi line string'''

# String
name = "OmKatkar"
print(name)

# Accessing characters in a string
print(name[0])
print(name[1])

# String slicing
print(name[0:5])

# Methods 
print(name.upper()) # converts to uppercase
print(name.lower()) # converts to lowercase
print(name.replace("om", "OM")) # replaces
print(name.isalpha()) # checks char
print(name.isnumeric()) # checks num

# concatination
first_str = "om"
second_str = "katkar"
concat_str = first_str + " " + second_str
print(concat_str)


print(len(concat_str))
