# Write a program that generates 10 random integers (from 0 to 30) and stores them in a list. 
# Then, the program should pass these numbers to a function that returns a sorted list (in ascending order) 
# containing the numbers.

######### SOLUTION #########

def my_function(numbers_list):
    return sorted(numbers_list)

import random

random_numbers = []

for i in range(10):
    number = random.randint(0, 30)
    random_numbers.append(number)

output = my_function(random_numbers)
print(output)