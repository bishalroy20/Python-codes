# Part 7 : while loop 

num1 = 1
while num1 <= 10:
    print(f"num is : {num1}")
    num1 += 1 


# break and continue
# Example 1: Using break

num = 10
while num <= 20:
    if num == 15:
        print("num is 15, breaking the loop")
        break  # Exit the loop when num is 15
    if num % 2 == 0:
        # print(f"num is even: {num}, continuing to next iteration")
        num += 1
        continue  # Skip the rest of the loop for even numbers
    print(f"num is odd: {num}")
    num += 1



# For loop
# Example 2: Using for loop with range

numbers = [1 ,2,3,4,5,6,7,8,9,10]

sum = 0
for num in numbers:
    print(num)
    sum += num

    if sum > 5:
        break 
print('total sum  : ' ,sum)

# Example 3: Using for loop char
text = 'tum itna jo muskura rahe ho'
for char in text:
    if char == ' ':
        print(' ')
    else:
        print(char)


# Example 4: Using for loop with range

# range(start, kothay stop korbe , koto step barbe)
for i in range(2 , 30 , 3):
    print(i)

""" Google :
kivabe ekta for loop diye value and index eksathe ber korbo . """
    

""" Home work
1. take 3 number and give me sum
2. Grade calculator in python
3. take 3 number and give me largest number  """