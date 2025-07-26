# Let's first overview the
# problem statement and understand precisely what we need to do.
# Problem1:
# Task 3: Matrix Multiplication
# Implement matrix multiplication (2D arrays).
# Ensure matrices are compatible for multiplication.
# Take input from user or define sample matrices in code.
# So let's start the coding to create two user-defined matrices:
def get_matrix_input(rows, cols):
    matrix = []
    print(f"Enter the elements for a {rows}x{cols} matrix:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            raise ValueError(f"Row {i + 1} must have exactly {cols} elements.")
        matrix.append(row)
    return matrix

def multiply_matrices(matrix__A, matrix__B):
    if len(matrix__A[0]) != len(matrix__B):
        raise ValueError("Matrices are not compatible for multiplication.")
    
    result = [[0 for _ in range(len(matrix__B[0]))] for _ in range(len(matrix__A))]
    
    for i in range(len(matrix__A)):
        for j in range(len(matrix__B[0])):
            for k in range(len(matrix__B)):
                result[i][j] += matrix__A[i][k] * matrix__B[k][j]
    
    return result

# Define the dimensions of the matrices
rows__A = int(input("Enter the number of rows for Matrix A: "))
cols__A = int(input("Enter the number of columns for Matrix A: "))
rows__B = int(input("Enter the number of rows for Matrix B: "))
cols__B = int(input("Enter the number of columns for Matrix B: "))
# Ensure the matrices are compatible for multiplication
if cols__A != rows__B:
    raise ValueError("Number of columns in Matrix A must equal number of rows in Matrix B.")

# Get user input for the matrices
matrix__A = get_matrix_input(rows__A, cols__A)
matrix__B = get_matrix_input(rows__B, cols__B)

# Perform matrix multiplication
result_matrix = multiply_matrices(matrix__A, matrix__B)
# Print the result
print("Result of Matrix Multiplication:")
for row in result_matrix:
    print(row)

# Let learn by one example how to use this program: 
# Example usage:
# Enter the number of rows for Matrix A: 3
# Enter the number of columns for Matrix A: 3
# Enter the number of rows for Matrix B: 3
# Enter the number of columns for Matrix B: 3
# Enter the elements for a 3x3 matrix:
# Row 1: 1 2 3
# Row 2: 4 5 6
# Row 3: 7 8 9
# Enter the elements for a 3x3 matrix:
# Row 1: 9 8 7
# Row 2: 6 5 4
# Row 3: 3 2 1
# Result of Matrix Multiplication:
# [30, 24, 18]
# [84, 69, 54]
# [138, 114, 90]
# Example Input:




