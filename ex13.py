# Given the following list:

my_list = [2, 3, 2, 2, 4, 2, 10, 8, 4, 3, 4, 5, 2, 1, 2, 3]

# Print how many occurrences of the number 2 there are in the list.

######### SOLUTION #########

counter = 0

for number in my_list:
    if number == 2:
        counter += 1

print(f"Occurrences of integer 2: {counter}")