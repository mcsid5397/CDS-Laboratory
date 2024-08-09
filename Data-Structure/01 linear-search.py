""" 
    Program: 01
    Program Name: 'Linear Search'
    Author: M. Praveen Kumar
"""

# Defining a list of numbers within the list
num_list = [9,0,3,6,7,4,2,8]
""" 
    List in Python are sequence datatype,
    Reffered to as mutable datatypes i.e, it can be updated once declared/initialized.
"""
# Entering a value as search key
search = int(input("Enter a number 0-9: "))

# Traversing within the list to find a match
for index in range(len(num_list)):
    if search == num_list[index]:
        print("The index of number",search,"is",index)
        print("The position of the number",search,"is",index+1)

# Block off the for loop
if search not in num_list:
    print("Enter a proper value")
