def threeSumClosest(nums: 'List[int]', target: int):
    nums.sort()
    i = len(nums) - 1
    compare = float('inf')
    value = None
    while i > -1:
        start = 0
        end = i - 1
        while start < end:
            t = nums[i]+nums[start]+nums[end]
            if abs(t-target ) < compare:
                compare = abs(t-target )
                value = t


            if t<target:
                start +=1
            elif t>target:
                end -=1
            if t==target:
                return value

        i-=1

    return value

print(threeSumClosest( [-1, 2, 1, -4],1))
print(threeSumClosest( [-1,0,1,2,-1,-4],0))
print(threeSumClosest( [1,2,4,8,16,32,64,128],82))
print(threeSumClosest( [-3,-2,-5,3,-4],-1))
print(threeSumClosest( [1,1,-1,-1,3],1))

