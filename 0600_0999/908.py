def MaxMin(input:"List[int]"): #this is to improve the performance , to get the max and min in one run.
    max = input[0]
    min = input[0]
    for i in input:
        if i > max:
            max = i
        if i < min:
            min = i
    return [min, max]

def smallestRangeI(A: 'List[int]', K: 'int'):
    bound = MaxMin(A)
    if bound[1]- bound[0] >= 2*K:
        return (bound[1]-K ) - (bound[0]+K)
    else:
        return 0

print(smallestRangeI([1], 0))
print(smallestRangeI( [0,10], 2))
print(smallestRangeI([1,3,6], 3))
print(smallestRangeI([1, 500, 400, 300], 20))
