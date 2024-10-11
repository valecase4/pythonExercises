# Write two functions:

# The first function should accept a string and check its length. 
# If the length of the input string is greater than 8, the second function is invoked by 
# passing the same string as a parameter.
# The second function should accept a string and returns the same 
# string coverted to uppercase.

######### SOLUTION #########

def function_1(input_string):
    if len(input_string) > 8:
        function_2(input_string)
    
    else:
        print("String is not greater than 8 characters.")

    
def function_2(input_string):
    print(input_string.upper())

function_1("Hello, world!")
function_1("Hello")
