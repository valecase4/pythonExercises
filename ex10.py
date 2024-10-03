# Create a function that takes a list of integers, checks if its length is odd, and 
# returns the mirrored list of integers if the length is odd.
# Note: neither reversed() methods nor slicing are allowed.

# Example:
# Input: [9, 3, 4, 2, 10]
# Output: [10, 2, 4, 3, 9]

######### SOLUTION #########

def my_function(input_list):
    if len(input_list) % 2 != 0:
        mirrored = []

        for i in range(len(input_list)):
            element = input_list[-i-1]
            mirrored.append(element)

        return mirrored
    
    return "The list length is not odd"

test_even = my_function([0, 4, 10, 2, 3, 2])
print(test_even)

test_odd = my_function([0, 3, 2, 4, 10, 3, 2])
print(test_odd)