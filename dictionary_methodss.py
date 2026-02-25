# Dictionary 

student = {
    "name": "om",
    "city": "pune",
    "age": 22
}

# accessing the value

print(student["name"])
print(student["city"])

# methods 

print(student.get("nameee"))  # None instead of error, returns value if present

student["company"] = "infosys"        # adding new key/value pair 
student["age"] = 19                   # updating an existing value

print(student)

students ={
    "name": "om",
    "city": "pune",
    "company": "infosys"
}

students.pop("city", None)            # remove key if it exists

print(students)

students.popitem()                    # removes last inserted pair
print(students)

del students["name"]                  # delete by key
print(students)

students.clear()                      # remove all pairs
print(students)

key_value = {
    "keys":  "value",
    "keys1": "value1"
}

print(key_value.keys())   # returns the keys 
print(key_value.values()) # returns the values
print(key_value.items())  # returns pairs as list of tuples
