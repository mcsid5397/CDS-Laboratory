""" 
    Program: 04
    Program Name: 'Selection Sort'
    Author: M. Praveen Kumar
"""

# Declaring list of numbers to perform sorting, particulary - Selection Sort 
number_list = [69,420,1,80880]


# Function to point out the minimum value and it's address in 'number_list'
def get_minimum_value_and_index(input_list):
    min_val = input_list[0] # Considering the first entry of the list to be the minimum value
    min_idx = 0 # List index stored to get the exact minimum value

    for list_idx in range(1, len(input_list)):
        if input_list[list_idx] < min_val:  # Comparing the rest of the list values with 'input_list[0]'
            min_val = input_list[list_idx]  # Update if required
            min_idx = list_idx  # Update if required
    return min_val, min_idx 

# Function to pop the minimum value and to make a list out of it
def selection_sort(input_list):
    sorted_list = []    # Empty list to store the list of values that turn to be minimal of all

    while input_list:
        min_val, min_idx = get_minimum_value_and_index(input_list)  # Assigning the values returned by the function within another variables
        sorted_list.append(min_val) # .append() passes argument 'input_value'
        input_list.pop(min_idx) # .pop() passes argument 'index'
    return sorted_list

'''
This Sorting technique simply selects the minimum value by traversing within the list of numbers given,
and performs sorting ascendingly for any list of number given.
'''
print(f'Original list: {number_list}')

# To check if the list is eligible to do Sorting
if len(number_list)==0:
    print("No values to perform sorting")
else:
    sorted_number_list = selection_sort(number_list)
    print(f"Sorted list: {sorted_number_list}")