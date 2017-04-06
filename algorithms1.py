array1 = [1,2,3,4,5,6]
array2 = [2,4,6,8,10]

def matrix(array1, array2, n):
    for i, j in zip(array1, array2):
        if j != (i * n):
            return False
    return True
        
        
def matrix2(array1, array2, n):
    for i, j in enumerate(array2):
        if j != (array1[i] * n):
            return False
    return True
    
print matrix(array1, array2, 2)
print matrix2(array1, array2, 2)