def minMoves(nums: 'List[int]'):
    #find the difference between each number and the minimum, and sum them.
    if len(nums)==0:
        return 0
    min_n = min(nums)
    sum  = 0
    for x in nums:
        sum+= x-min_n
    return sum

print(minMoves([1,2,3]))
print(minMoves([1,1,1]))
print(minMoves([]))
print(minMoves([1,1]))
print(minMoves([-1,3,5,7,27,6,4,423,5674,436,2313,0]))
