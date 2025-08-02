# part 17 : tuple ()

def multiple():
    return 3,4

# print(multiple())

things = 'pen' , 'tripod' , 'water bottol' , 'charger' , 'phone' , 'webcam' , 'sunglass'

print(things[0])
print(things[-3])
print(things[::-1])
print(things[3:6])

# not supported in assignment , cannot assign values .

print(len(things))

mega = ([2,3,4],[1,5,3])
print(type(mega))

mega[0][1] = 44

print(mega[0][1])  #it can changeable


