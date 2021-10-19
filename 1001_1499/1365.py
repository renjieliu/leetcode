class Solution:
    def smallerNumbersThanCurrent(self, nums: 'List[int]') -> 'List[int]':
        output =[]
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[j] < nums[i] and i!=j:
                    cnt +=1
            output.append(cnt)
        return output