class Solution:
    def partitionArray(self, nums: 'List[int]', k: int) -> int: #O(NlogN | 1)
        nums.sort()
        currMin = nums[0] #local mininum
        cnt = 1 #number of partitions
        for n in nums[1:]: #go through the list, see if curr number - currMin is > k
            if n-currMin > k:
                cnt += 1 
                currMin = n
        return cnt 

