
s1 = 'Hello'
s2 = "World"
s3 = """This is
a multi-line string"""

a = "Hello"
b = "World"
print(a + " " + b)   # Hello World
print("Hi! " * 3)
text = "Python"
print(text[0])      # P
print(text[0:4])    # Pyth
print(text[-1])     # n
s = "python programming"


# | Method                       | Description              |
# | ---------------------------- | ------------------------ |
# | `s.upper()`                  | Converts to uppercase    |
# | `s.lower()`                  | Converts to lowercase    |
# | `s.capitalize()`             | Capitalizes first letter |
# | `s.title()`                  | Capitalizes each word    |
# | `s.strip()`                  | Removes whitespace       |
# | `s.replace("python","java")` | Replaces text            |
# | `s.split()`                  | Splits into list         |
# | `" ".join(list)`             | Joins list into string   |
# | `s.find("pro")`              | Returns index            |
# | `s.count("p")`               | Counts occurrences       |
# | `s.startswith("py")`         | Checks beginning         |
# | `s.endswith("ing")`          | Checks ending            |


name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")

print("My name is {} and I am {} years old.".format(name, age))

# | Escape | Meaning      |
# | ------ | ------------ |
# | `\n`   | New line     |
# | `\t`   | Tab          |
# | `\\`   | Backslash    |
# | `\'`   | Single quote |
# | `\"`   | Double quote |


#===========================================================
#           Exception Handling in python

#ex 1
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")

#ex 2
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print("Success:", x)


#ex 3
try:
    num = int(input())
    result = 10 / num
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed")



#ex 4
age = 4
if age < 0:
    raise ValueError("Age cannot be negative")



#ex 5 custom
class MyError(Exception):
    pass

raise MyError("This is a custom error")