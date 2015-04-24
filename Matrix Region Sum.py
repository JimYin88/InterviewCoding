def matrix_region_sum(matrix, A, D):
    result = 0
    for i in range(A[0], D[0] + 1):
        for j in range(A[1], D[1] + 1):
            result += matrix[i][j]
    return result
