# Part 8 : Functions

# Example 1 : define

def double(num):
    result = num*2
    print(result)

double(5)

# Example 2 : return
def double_return(num):
    result = num * 2
    return result

ans = double_return(5)
print(ans)

# Example 3 : multiple parameters
def add_numbers(num1, num2 , num3):
    return num1 + num2 + num3

ans = add_numbers(5, 10, 15)
print(ans)


# Part 9 : default parameter and args

# def sum(num1 , num2 , num3 = 0):
def sum(num1 , num2 , num3 = 0 , num4 = 0 , num5 = 0):
    result = num1 + num2 + num3
    return result

# total = sum(5, 10)
total = sum(5, 10 , 90)
print(total)


# Example 4 : args


def all_sum(num1 , *numbers):
    # print(numbers) tuple hisebe dey value
    sum = 0
    for i in numbers:
        print(i)
        sum += i
    return sum

total = all_sum(1, 2, 3, 4, 5)
print('all sum : ' , total)

