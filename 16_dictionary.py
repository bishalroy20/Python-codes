# Part 19 : Dictionary

person1 = [ 'kala mia' , 'chander deshe' , 22 , 'student']

""" 
key value pair
dictionary
object
hash table
overlap with set
 """

person = {'name' : 'kala' , 'address' : 'kalipur' , 'age' : 22 , 'job' : 'bekar'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())

person['langauge'] = 'python'

del person['age']


# enamurate

num = [15 ,25,2,54,58]

for i,n in enumerate(num):
    print(i , n)




# part 10 : Built in Modules

from math import *
from random import *
from time import sleep
result = ceil(4.6)
result = floor(4.6)
print(result)

print(random())
print(randint(1,50))
sleep(3)
print(choice(['sakib' , 'mush' , 'ta' , 'fiz' , 'awd']))



# try-except-finaly
# file read , write , append