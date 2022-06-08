class Solution:
    def minMaxGame(self, nums: 'List[int]') -> int: #(logN | N)
        def helper(arr): #simulate the requirement
            output=[]
            for i in range(len(arr)//2):
                output.append(min(arr[2*i], arr[2*i+1]) if i % 2 == 0 else max(arr[2*i], arr[2*i+1]))
            return output
        
        while len(nums) > 1: # keep simulating, until the length is <= 1
            nums = helper(nums)
        return nums[0]
    
