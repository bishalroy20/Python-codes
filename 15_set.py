# Part 18 : set

""" 
list --> []
tuple --> ()
set --> {}

 """
# set : unique items collection

numbers = [12 ,25,44,78,96,33 , 33 , 12 , 25]

# print(numbers)
numberset = set(numbers)
# print(numberset)

numberset.add(55)
numberset.remove(25)

# can't assign value .
print(numberset)


for item in numberset:
    print(item)


if 9 in numberset:
    print('9 exists')

elif 98 in numberset:
    print('98 exists')


# union
a = { 10,20,30}
b = {25 , 65 , 85 , 20}
print(a & b)
print(a | b)


# set method
