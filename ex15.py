# Given the following list of integers:

my_list = [9, 5, 12, 34, 11, 23, 3, 5, 9, 4, 4, 12, 50, 23, 10, 8, 10]

# Write a program that stores the squares of even numbers in a new list, ensuring no duplicates.

######### SOLUTION #########

new_list = []

for number in my_list:
    if number % 2 != 0:
        continue

    if number * number in new_list:
        continue

    new_list.append(number * number)

print(new_list)