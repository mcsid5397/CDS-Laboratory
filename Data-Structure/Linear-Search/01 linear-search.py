""" 
    Program: 01
    Program Name: 'Linear Search'
    Author: M. Praveen Kumar
"""


# Defining a function  to the operation of traversing
def find_num_postion(num_list, search):

    # Traversing within the list to find a match
    for index in range(len(num_list)):
        if search == num_list[index]:
            print("The index of number", search, "is", index)
            print("The position of the number", search, "is", index + 1)
            return  # Breaks when the conditions are satisfied and returns the index value

    # If the loop is terminated without finding the number
    if search not in num_list:
        print("Enter a proper value")


# Example usage
# Defining a list of numbers within the list "num_list"
num_list = [9, 0, 3, 6, 7, 4, 2, 8]
""" 
    List in Python are sequence datatype,
    Reffered to as mutable datatypes i.e, it can be updated once declared/initialized.
"""
# Entering a value as search key
search = int(input("Enter a number 0-9: "))
# Calling the function with initialized variables
find_num_postion(num_list, search)
