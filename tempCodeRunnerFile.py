player = ['sakib' , ' mushfiq' , 'masrafi']

age = [25 , 26 , 18]

age_comb = []

for p in player:
    print('player : ',p)
    for a in age:
        age_comb.append([p , a])

print(age_comb)