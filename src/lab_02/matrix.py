def transpose(mat):
    if not mat:
        return []
    
    rows = len(mat)
    cols = len(mat[0])
    
    for row in mat:
        if len(row) != cols:
            raise(ValueError)
    
    result = []
    
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(mat[i][j])
        result.append(new_row)
    
    return result

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))



def row_sums(mat):
    if not mat:
        return []    
    rows = len(mat)
    cols = len(mat[0])

    for row in mat:
        if len(row) != cols:
            raise(ValueError)        
    sums = []
    for row in mat:          
        total = sum(row)      
        sums.append(total)    
    return sums
print(row_sums([[1,2,3], [4,5,6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0,0], [0,0]]))
print(row_sums([[1, 2], [3]]))



def col_sums(mat):
    if not mat:
        return []
    rows = len(mat)
    cols = len(mat[0])
    for row in mat:
        if len(row) != cols:
            raise(ValueError)
    
    sums = []
    for j in range(cols):
        column_sum = 0
        for i in range(rows):
            column_sum += mat[i][j]
        sums.append(column_sum)
    return sums

print(col_sums([[1, 2, 3], [4, 5, 6]]))  
print(col_sums([[-1, 1], [10, -10]]))    
print(col_sums([[0, 0], [0, 0]]))        
print(col_sums([[1, 2], [3]])) 
