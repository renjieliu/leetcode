class Solution:
    def minDifference(self, nums: 'List[int]') -> int:
        if len(nums) <= 3 :return 0
        else: #sliding window from left 3 to right 3
            nums.sort()
            output = nums[-1] - nums[0]
            for i in range(4):
                if i < 3:
                    arr = nums[i:-(3-i)]
                elif i == 3:
                    arr = nums[3:]
                #print(arr)
                output = min(output, arr[-1] - arr[0])
            return output
