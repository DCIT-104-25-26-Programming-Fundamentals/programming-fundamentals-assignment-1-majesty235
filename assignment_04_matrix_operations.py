# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def read_matrix(rows, cols, label=""):
    """Reads a matrix of size rows x cols from the user, one row at a time."""
    matrix = []
    for i in range(rows):
        while True:
            values = input(f"Enter row {i + 1}{label}: ").split()
            if len(values) != cols:
                print(f"Error: expected {cols} value(s), got {len(values)}. Try again.")
                continue
            matrix.append([float(v) for v in values])
            break
    return matrix


def print_matrix(matrix, title=""):
    """Displays a matrix in a neat, aligned grid format."""
    if title:
        print(title)

    # Determine the widest formatted number so columns line up
    formatted = [[format_num(val) for val in row] for row in matrix]
    width = max(len(val) for row in formatted for val in row)

    for row in formatted:
        print("  ".join(val.rjust(width) for val in row))
    print()


def format_num(x):
    """Formats a number without a trailing .0 for whole numbers."""
    return f"{x:g}"


def transpose_matrix(matrix):
    """Returns the transpose of the given matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(a, b):
    """Returns the element-wise sum of two same-size matrices."""
    rows = len(a)
    cols = len(a[0])

    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]

    return result


def multiply_matrices(a, b):
    """Returns the matrix product A x B using nested loops."""
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])

    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            result[i][j] = total

    return result


def part_a_transpose():
    print("\n--- Part A: Transpose a Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = read_matrix(rows, cols)

    print_matrix(matrix, "\nOriginal Matrix:")
    print_matrix(transpose_matrix(matrix), "Transposed Matrix:")


def part_b_addition():
    print("\n--- Part B: Add Two Matrices ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("\nMatrix A:")
    matrix_a = read_matrix(rows, cols)

    print("\nMatrix B:")
    matrix_b = read_matrix(rows, cols)

    result = add_matrices(matrix_a, matrix_b)

    print_matrix(matrix_a, "\nMatrix A:")
    print_matrix(matrix_b, "Matrix B:")
    print_matrix(result, "Sum (A + B):")


def part_c_multiplication():
    print("\n--- Part C: Multiply Two Matrices ---")
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A (= rows of Matrix B): "))
    p = int(input("Enter columns of Matrix B: "))

    print("\nMatrix A:")
    matrix_a = read_matrix(m, n)

    print("\nMatrix B:")
    matrix_b = read_matrix(n, p)

    result = multiply_matrices(matrix_a, matrix_b)

    print_matrix(matrix_a, "\nMatrix A:")
    print_matrix(matrix_b, "Matrix B:")
    print_matrix(result, "Product (A x B):")


def main():
    print("Matrix Operations")
    print("1. Transpose a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")

    choice = input("Choose an operation (1-3): ").strip()

    if choice == "1":
        part_a_transpose()
    elif choice == "2":
        part_b_addition()
    elif choice == "3":
        part_c_multiplication()
    else:
        print("Error: Invalid choice.")


if __name__ == "__main__":
    main()