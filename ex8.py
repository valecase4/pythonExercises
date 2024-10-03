# Write a function that takes a list and returns a new list containing only the duplicate elements.

######### SOLUTION #########

def my_function(input_list):
    duplicates = []

    for item in input_list:
        occurences = input_list.count(item)
        
        if occurences > 1:
            if not item in duplicates:
                duplicates.append(item)
    
    return duplicates

test = my_function([9, 9, 3, 2, 5, 5, 10, 3, 2, 1, 0, 9, 8, 7, 3])
print(test)

