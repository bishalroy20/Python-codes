# Part 12 : scope


# Example 1: Local and Global Scope
balance = 3000

def buy_things(item , price):
    balance = balance - price  # This will raise an UnboundLocalError because balance is referenced before assignment and it can't change the global variable

    # print(balance)
    print(f'after buying {item} : {balance}')
    dream_phone = "iPhone 15"

#print(dream_phone)  # This will raise an error because dream_phone is not defined in the global scope

# buy_things("laptop", 1500)

# solution of Example 1

balance = 3000
def buy_things(item, price):
    balance = 1200
    print(f'before buying {item} : {balance}')
    balance = balance - price  # This will now work because balance is defined locally
    print(f'after buying {item} : {balance}')


# buy_things("laptop", 1000)



# Example 2: Using global keyword
balance = 3000      
def buy_things(item, price):
    dream_pjone = "iPhone 15"
    global balance  # Declare balance as global to modify the global variable
    print(f'before buying {item} : {balance}')
    balance = balance - price
    print(f'after buying {item} : {balance}')

buy_things("laptop", 1000)
print(f'final balance : {balance}')  # This will now show the updated balance


""" 
local scope variable can not access outside the function.
you can access global variable without using global keyword .
But if you want to modify the global variable you have to use global keyword"""