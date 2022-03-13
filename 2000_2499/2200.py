class Solution:
    def findKDistantIndices(self, nums: 'List[int]', key: int, k: int) -> 'List[int]': #O(n2)
        arr = [i for i, n in enumerate(nums) if n == key] # find all the index with key
        output = []
        for i in range(len(nums)): #check one by one to see if it can satisfy the condition
            for a in arr:
                if abs(a-i) <=k:
                    output.append(i)
                    break 
        return output

    
    
    
