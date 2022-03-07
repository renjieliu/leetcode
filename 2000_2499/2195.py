class Solution:
    def minimalKSum(self, nums: 'List[int]', k: int) -> int:
        gauss = lambda a, b: ((a+b)*(b-a+1)//2) if a<=b else 0 # total from a to b
        nums.sort()
        nums.insert(0, 0) #to make the calculation easier, put non-exist 0 to the front
        output = 0
        
        for i in range(1, len(nums)): # for each numbers, check how many number can be plugged in. 
            s = nums[i-1]+1
            e = min(nums[i-1]+k, nums[i]-1)
            output += gauss(s, e)
            #print(nums[i-1], nums[i],'--',  s, e)
            k -= ( (e-s+1) if e>=s else 0)
            if k == 0:
                return output
        
        return output+gauss(nums[-1]+1, nums[-1]+k) #add the remaining k to the output
 

        