# Write a function that accepts two integers and returns a dictionary that stores 
# the result of their addition, subtraction, product and division.

# Example:
# Input: 4, 5
# Output: {
# “addition”: 9,
# “subtraction”: -1,
# “product”: 20,
# “division”: 0.8
# }

######### SOLUTION #########

def my_function(a, b):
    return {
        "addition": a + b,
        "subtraction": a - b,
        "product": a * b,
        "division": a / b
    }

output = my_function(4, 5)
print(output)