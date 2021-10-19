def prefixesDivBy5(A: 'List[int]'):
    output = []
    c = ""
    for i in range(len(A)):
        c+=str(A[i])
        if  int(c,2)%5==0:
            output.append(True)
        else:
            output.append(False)

    return output

print(prefixesDivBy5([0,1,1]))
print(prefixesDivBy5([1,1,1]))
print(prefixesDivBy5([0,1,1,1,1,1]))
print(prefixesDivBy5([1,1,1,0,1]))
print(prefixesDivBy5([1,1,0,0,0,1,0,0,1]))
#[false,false,false,false,false,false,false,false,false]


