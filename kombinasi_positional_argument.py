def matrix_multiply_scalar(matrix, scalar = 1): 
    res = [] 
    for row in matrix: 
        res.append([cell * scalar for cell in row])