class Solution:
    def applyOperations(self, nums: 'List[int]') -> 'List[int]': # O( N | N )
        output = []
        zero = 0
        i = 0
        while i < len(nums)-1: # go through the array, change the number according to the requirements
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            i += 1 
        
        for n in nums:
            if n == 0:
                zero += 1 
            else:
                output.append(n)
        
        return output + [0]*zero # put all the zeroes to the end of the array
    

