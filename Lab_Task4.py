# my_tuple = (10, 20, 30, "Python")
# print(my_tuple)   

# numbers = (1, 2, 3, 4, 5)
# print(numbers[0])      # Output: 1
# print(numbers[1:4])    # Output: (2, 3, 4)

# a = (1, 2)
# b = (3, 4)
# print(a + b)       # Output: (1, 2, 3, 4)
# print(a * 3)       # Output: (1, 2, 1, 2, 1, 2)
# print(2 in a)      # Output: True


# t = (1, 2, 2, 3, 4)
# print(t.count(2))   # Output: 2
# print(t.index(3))   # Output: 3

# nested = ((1, 2), (3, 4), (5, 6))
# print(nested[1])       # Output: (3, 4)
# print(nested[1][0])    # Output: 3

# # Packing
# packed = (10, 20, 30)

# # Unpacking
# x, y, z = packed
# print(x, y, z)   # Output: 10 20 30

# coordinates = (10, 20)
# location_dict = {coordinates: "Park"}
# print(location_dict)   # Output: {(10, 20): 'Park'}



# ================================
# Dictionaries in Python         
# ================================

# 1. Creating a dictionary
student = {"name": "Alice", "age": 21, "course": "Python"}
print("Initial dictionary:", student)

# 2. Accessing elements
print("Name:", student["name"])                 # Direct access
print("Age:", student.get("age"))               # Using get()
print("Grade:", student.get("grade", "N/A"))    # Safe access with default

# 3. Modifying dictionary
student["age"] = 22          # Update value
student["course"] = "AI"     # Add new key-value
del student["name"]          # Delete a key
print("Modified dictionary:", student)

# 4. Dictionary methods
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

student.update({"semester": "Spring"})
print("After update:", student)

student.pop("age")
print("After pop:", student)



# 5. Nested dictionaries
students = {
    "101": {"name": "Alice", "age": 21},
    "102": {"name": "Bob", "age": 22}
}
print("Nested dictionary:", students)
print("Student 101 name:", students["101"]["name"])

# 6. Iterating through dictionary
print("Iterating through student dictionary:")
for key in student:
    print(key, ":", student[key])

# 7. Use case example
users = {"alice": "password123", "bob": "qwerty"}
print("Bob's password:", users["bob"])