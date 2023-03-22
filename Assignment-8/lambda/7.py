''''Write a Python program to sort a given matrix in ascending order according to
the sum of its rows using lambda.
Original Matrix: [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
Sort the said matrix in ascending order according to the sum of its rows [[1, 1, 1],[1, 2, 3], [2, 4, 5]]'''

original_matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
original_matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
sorted_matrix1 = sorted(original_matrix1, key=lambda x: sum(x))
sorted_matrix2 = sorted(original_matrix2, key=lambda x: sum(x))
print("Original Matrix 1:", original_matrix1)
print("Sorted matrix 1 in ascending order according to the sum of its rows:", sorted_matrix1)
print("Original Matrix 2:", original_matrix2)
print("Sorted matrix 2 in ascending order according to the sum of its rows:", sorted_matrix2)