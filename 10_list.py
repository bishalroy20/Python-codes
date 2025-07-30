# Part 14 : lists / arrays /  collections is same

# index    0  1  2  3  4  5  6  7  8   9 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# index   -10 -9 -8 -7 -6 -5 -4 -3 -2  -1


# print(numbers[3])  
# print(numbers[-3])  

# list (start : end )
print(numbers[2:8])
print(numbers[8:2]) 
# list (start : end , step)
print(numbers[2:8:2])  
print(numbers[7:2:-1]) 

print(numbers[::2])  # print all even index
print(numbers[::-1])  # print in reverse order

print(numbers[2:])  # print from index 2 to end
print(numbers[:5])  # print from start to index 5
print(numbers[:])  # print all 

""" Google :
python list method (dsa) 

"""

arr = [1,2,3,4,5,6,7,8,9,0 , 10 , 10 , 10]

arr.append(11)
print(arr)

arr.insert(9 , 10) #(index , value)

arr.remove(1) #if 1 is not it will show an error
if 2 in arr:
    arr.remove(2)

last = arr.pop() # last value delete

# arr.clear()  #remove all elements from arr

index = arr.index( 5)  # 5 value er index koto
print('5 er index : ' ,index)

num = arr.count(10)  #it gives the frequency of 10

arr.reverse()

arr.sort()

arr1 = [1,2,3,4,5,6,7,8,9,0 , 10 , 10 , 10]
arr2 = arr1.copy()

print(arr2)




