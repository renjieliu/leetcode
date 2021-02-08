def generate(numRows: int):
    if numRows ==0:
        return []
    if numRows ==1 :
        return [[1]]
    elif numRows == 2:
        return [[1],[1,1]]

    else:
        output=[[1], [1,1]]
        for i in range(2,numRows): #for the rows.
            temp = [1]
            for j in range(0,i-1): # for the columns
                t = output[i-1][j] + output[i-1][j+1]
                temp.append(t)
            temp.append(1)
            output.append(temp)

    return output


print(generate(1))
print(generate(2))
print(generate(3))
print(generate(4))
print(generate(5))
print(generate(6))



