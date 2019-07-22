def maxAbsValExpr(arr1: 'List[int]', arr2: 'List[int]'):
    a1, a2, a3, a4 = [],[],[],[]
    cnt = len(arr1)
    for i in range(cnt):
        a1.append( arr1[i] + arr2[i] + i)
        a2.append( -arr1[i] + arr2[i] + i)
        a3.append( arr1[i] - arr2[i] + i)
        a4.append( -arr1[i]- arr2[i] + i)

    return max( max(a1)-min(a1)  , max(a2)-min(a2) , max(a3)-min(a3) , max(a4)-min(a4)   )


print(maxAbsValExpr(arr1 = [1,2,3,4], arr2 = [-1,4,5,6]))
print(maxAbsValExpr(arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]))






