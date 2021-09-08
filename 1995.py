class Solution:
    def countQuadruplets(self, nums: 'List[int]') -> int:
        cnt = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    for m in range(k+1, len(nums)):
                        if nums[i] + nums[j] + nums[k] - nums[m] == 0:
                            cnt +=1
        return cnt



