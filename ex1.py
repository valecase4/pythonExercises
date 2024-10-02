# Given the following list

my_list = ["banana", "apple", "orange", "banana", "cherry", "peach", "apple", "pear", "pear", "banana", "apple"]

# Write a program that counts the frequency of each item in the list and stores the results in a dictionary

######### SOLUTION

my_dictionary = {}

for item in my_list:
    if not item in my_dictionary:
        my_dictionary[item] = 1
    else:
        my_dictionary[item] += 1

print(my_dictionary)