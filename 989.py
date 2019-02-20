def addToArrayForm(A: 'List[int]', K: 'int'):
    temp = ""
    for i in A:
        temp+=str(i)

    output= []
    for i in str(int(temp) +K):
        output.append(int(i))

    return output

print(addToArrayForm([1,2,0,0], 34 ))
print(addToArrayForm([2,7,4], 181 ))
print(addToArrayForm([2,1,5], 806 ))
