class Solution:
    def elementInNums(self, nums: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        lkp = [] # all the possible transformation 
        for i in range(len(nums)+1): #need to add [] to the end of first phase
            lkp.append(nums[i:])
        for i in range(len(nums)-1): #no need to add the original to the lkp array
            lkp.append(lkp[-1] + [nums[i]])
        output = []
        for times, idx in queries:
            loc = times%len(lkp)
            if idx >= len(lkp[loc]):
                output.append(-1)
            else:
                output.append(lkp[loc][idx])
        return output

    

