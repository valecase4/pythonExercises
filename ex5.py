# Write a function that generates 20 random integers (from 0 to 100) and returns 
# a dictionary that stores the count of even and odd numbers.

######### SOLUTION #########

import random

def my_function():

    counter_dict = {
        "even": 0,
        "odd": 0
    }

    for i in range(20):
        random_number = random.randint(0, 100)

        print(random_number) # test

        if random_number % 2 == 0:
            counter_dict["even"] += 1
        else:
            counter_dict["odd"] += 1

    return counter_dict

output = my_function()
print(output)