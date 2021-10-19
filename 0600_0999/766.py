def isToeplitzMatrix(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """
    checkLength = len(matrix[0])-1
    for i in range(0, checkLength):
        for j in range(0, len(matrix)-1):
            if matrix[j][i] != matrix[j+1][i+1]:
                return False

    return True



print(isToeplitzMatrix(  [[1,2,3,4],[5,1,2,3],[9,5,1,2]] ))
print(isToeplitzMatrix(  [[1,2],[2,2]] ))





