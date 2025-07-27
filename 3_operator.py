# Part 5 : Operators

# Arithmetic Operators ( + , - , * , / , // , % , ** )
num1 = 43
num2 = 5
print(f"num1 + num2 = {num1 + num2}")
print(f"num1 - num2 = {num1 - num2}")
print(f"num1 * num2 = {num1 * num2}")   
print(f"num1 / num2 = {num1 / num2}")
print(10/3)
print(f"num1 // num2 = {num1 // num2}")  # Floor division or integer division
print(f"num1 % num2 = {num1 % num2}")    # Modulus or remainder
print(f"num1 ** num2 = {num1 ** num2}")  # Exponentiation


# Comparison Operators ( == , != , > , < , >= , <= )
# In python there is no increment or decrement operator like ++ or --

# Part 6 : conditional statements

""" in , not , not in , and , or , is , is not.
a = 10
a = a + 2
a += 2 """

# Example 1
a = 7
if a > 5:
    print("a is greater than 5")
else:
    print("a is not greater than 5")

# Example 2
b = 4
if b > 5 :
    print("b is greater than 5")
elif b > 4:
    print("b is greater than 4")
elif b == 4:
    print("b is equal to 4")
else:
    print("b is less than 4")

# Example 3
boss = False
if boss is True:
    print("I am the boss")
    print("sobar chakri khabo")
else:
    print("I am a employee")

# Example 4 (Nested conditions)

boss = True
boss_age = 55
my_salary = 35000

if boss is True:
    print("Boss you are joss")
    if boss_age > 50:
        print("Boss you are sweet sixteen")
        print("Boss re tel martesi , he he he")
        if my_salary < 50000 or my_salary < 40000:
            print("Boss you are rich")
            print("maine bariye den na please")
    else:
        print("Boss you are not sweet sixteen")
        
else:
    print("come after 5 pm")