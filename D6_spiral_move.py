def print_spiral(matrix):
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    spiral_order = []
    
    while top <= bottom and left <= right:
        # Traverse from left to right along the top row
        for i in range(left, right + 1):
            spiral_order.append(matrix[top][i])
        top += 1

        # Traverse from top to bottom along the right column
        for i in range(top, bottom + 1):
            spiral_order.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            # Traverse from right to left along the bottom row
            for i in range(right, left - 1, -1):
                spiral_order.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            # Traverse from bottom to top along the left column
            for i in range(bottom, top - 1, -1):
                spiral_order.append(matrix[i][left])
            left += 1

    return spiral_order


def main():
    # Input matrix dimensions
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Input matrix elements
    print("Enter the matrix elements row by row:")
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Print the matrix in spiral order
    spiral = print_spiral(matrix)
    print("Spiral order of the matrix is:")
    print(spiral)


if __name__ == "__main__":
    main()
