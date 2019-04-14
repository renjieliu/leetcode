def minimumTotal(triangle: 'List[List[int]]'):
    if len(triangle)==1 :
        return min(triangle[0])
    else:
        path =0
        output = triangle.copy()
        output[1][0] += output[0][0]
        output[1][1] += output[0][0]
        for i in range(2, len(triangle)):
            for j in range(len(triangle[i])):
                if j==0:
                    output[i][j] += output[i-1][0]
                elif j==len(triangle[i])-1:
                    output[i][j] += output[i-1][-1]
                else:
                    output[i][j] += min(output[i-1][j], output[i-1][j-1])

        return min(output[-1])

print(minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))