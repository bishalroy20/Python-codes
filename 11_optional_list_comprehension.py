# Part 15 : list comprehension


number = [12,25,147,36,50,80,99,25,15,45]

odd = []

for num in number:
    if num%2 == 1 and num%5 == 0:
        odd.append(num)

print(odd)

# in a complex way we can write 

odd_num = [num for num in number if num%2 == 1 if num%5 == 0]
print(odd_num)

#----------------------- Example---------------------

player = ['sakib' , ' mushfiq' , 'masrafi']

age = [25 , 26 , 18]

age_comb = []

for p in player:
    print('player : ',p)
    for a in age:
        age_comb.append([p , a])

print(age_comb)


# or

age_comb2 = [[p,a] for p in player for a in age]
print(age_comb2)