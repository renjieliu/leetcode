def minSubArrayLen(s: int, nums:'List[int]'):
    l, r  = 0,0
    curr = 0
    output = float('inf')
    while r < len(nums) :
        curr += nums[r]
        if curr >=s:
            while curr >= s:
                curr-=nums[l]
                output = min(output, r-l+1)
                l+=1
        r+=1

    return output if output!=float('inf') else 0

print(minSubArrayLen(s = 7, nums = [2,3,1,2,4,3]))