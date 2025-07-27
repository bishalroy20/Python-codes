# Part 10 : kwargs

def full_name(first , last ):
    name = f"{first} {last}"
    return name

# name = full_name("Anthony" , "Gonsalves")
name = full_name(last = "Gonsalves" , first = "Anthony")
print(name)


# Example 1 : kwargs with default value
def famous_name(first , last , title , addition):
    name = f'{title} {first} {last} '
    return name

print(famous_name("Anthony" , "Gonsalves" , "Mr." , "CEO"))

# Example 2 : multiple kwargs

def famous_name(first , last , **addition):
    name = f' {first} {last} '
    # print(addition['title'])
    for key,value in addition.items():
        print(key , value)
    return name

# print(famous_name("Anthony" , "Gonsalves" , title="Mr." , addition="CEO"))
print(famous_name(first="Anthony" , last="Gonsalves" , title="Mr." , addition="CEO" , last2="Gonsalves2"))



# Example 3 : multiple kwargs with default value
def famous_name(first , last , title="Mr." , addition="CEO"):
    name = f'{title} {first} {last} '
    return name 

print(famous_name("Anthony" , "Gonsalves"))
print(famous_name("Anthony" , "Gonsalves" , title="Dr." , addition="CTO"))



# Example 4 : multiple kwargs with default value and order
def famous_name(first , last , title="Mr." , addition="CEO", **kwargs):
    name = f'{title} {first} {last} '
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    return name 

print(famous_name("Anthony" , "Gonsalves", title="Dr.", addition="CTO", last2="Gonsalves2", age=30, country="USA"))


# Part 11 : Multiple returns

def a_lot(num1 , num2):
    sum_result = num1 + num2
    diff_result = num1 - num2
    mul = num1 * num2
    # return [sum_result, diff_result, mul]  # Returning a list with multiple values []
    return sum_result, diff_result    # Returning multiple values as a tuple ()

everything = a_lot(10, 5)
print(everything)  # Output: (15, 5)