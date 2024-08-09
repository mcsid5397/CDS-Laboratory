""" 
    Program: 01
    Program Name: 'Linear Search'
    Author: M. Praveen Kumar
"""

# Defining a list of numbers within the list
num_list = [9,0,3,6,7,4,2,8]

# Entering a value as search key
search = input("Enter a number 0-10: ")

# Traversing within the list to find a match
for index in range(len(num_list)):
    if search == num_list[index]:
        print(f"The index of the search key is {index} and is found in the postion {index+1}")

# Block off the for loop
if search not in num_list:
    print(f"The value {search} couldn't be found within the list")
