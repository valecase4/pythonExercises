# Given the following 4x4 matrix, find the column with the highest sum of its elements

matrix = [
    [5, 2, 0, 1],
    [1, 4, 10, 1],
    [5, 2, 7, 6],
    [2, 2, 4, 9]
]

######### SOLUTION #########

rows_number = len(matrix)
columns_number = len(matrix[0])

max_value = 0
max_column = None

for k in range(rows_number):
    total = 0
    for j in range(columns_number):
        element = matrix[j][k]
        total += element
    if total > max_value:
        max_value = total
        max_column = k

print(f"Best column: {max_column}")
        

