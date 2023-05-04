#[[2, 1, 2, 2]] 
#[[1, 1, 2, 3]]
#[[1, 2, 2, 2]]
#[[2, 3, 3, 2]]
#
#flood fill connected 2's at point (0, 2) to 0's
#
#output =>
#
#[[2, 1, 0, 0]]
#[[1, 1, 0, 3]]
#[[1, 0, 0, 0]]
#[[2, 3, 3, 0]]



from collections import deque
from pprint import pprint

def flood_fill(matrix, start_row, start_col, new_value):
    old_value = matrix[start_row][start_col]

    if old_value == new_value:
        return matrix
    
    #dimensions
    n_rows = len(matrix)
    n_columns = len(matrix[0])
    queue = deque([(start_row, start_col)])

    while queue:
        row, col = queue.popleft()

        if matrix[row][col] == old_value:
            matrix[row][col] = new_value

            for r, c in [
                (row-1, col), (row+1, col), (row, col-1), (row, col+1)
            ]:
                if 0 <= r < n_rows and 0 <= c < n_columns:
                    queue.append((r, c))

    return matrix

if __name__ == "__main__":

    matrix = [
        [2, 1, 2, 2],
        [1, 1, 2, 3],
        [1, 2, 2, 2],
        [2, 3, 3, 2]
    ]

    print('Old matrix:\n')

    for row in matrix:
        print(row)

    print('\n')
    
    matrix_transformed = flood_fill(matrix, 0, 2, 0)

    print('\n')

    print('New matrix:\n')

    for row in matrix_transformed:
        print(row)




