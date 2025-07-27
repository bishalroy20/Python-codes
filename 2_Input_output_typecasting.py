# part 3 : Take input

print("Give me money ")
input()
# input('Give me money')

qty = input()
print(f"Money given : {qty} .")
print("Money given : " , qty)

# Example of input

money1 = input("Give me money 1 : ")
money2 = input("Give me money 2 : ")

print(type(money1))

print(f"i got money from money1 : {money1} and money2 : {money2}")

total = money1 + money2
print(f"Total money is : {total}")

# both the money are string type . so if we want to see the total as number we need to convert it to int or float

# part 4 : Type casting
# int() , float() , str()
total = int(money1) + int(money2)
print(f"Total money is : {total}")

""" Google : 
1. convert number to string : str
2. convert decimal to integer : int
3. convert string to float : float
4. convert string to integer : int
5. convert integer to string : str
optional : list , tuple , hex , oct , bin"""