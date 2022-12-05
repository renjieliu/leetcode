class Solution:
    def minimumAverageDifference(self, nums: 'List[int]') -> int: # O( N | 1 )
        total = sum(nums) 
        mi = float('inf')
        output = -1 
        curr = 0 
        for i, n in enumerate(nums): # prefix sum, and find the first Avg and Last Avg. 
            curr += n 
            firstAvg = curr // (i+1) 
            lastCnt = len(nums)-1-i
            lastAvg = 0 if lastCnt == 0 else (total - curr) // lastCnt 
            diff = abs(firstAvg - lastAvg)
            if diff < mi:
                mi = diff 
                output = i
        
        return output




# previous solution

# class Solution:
#     def minimumAverageDifference(self, nums: 'List[int]') -> int:
#         prefix = [nums[0]] # prefix sum
#         for n in nums[1:]:
#             prefix.append(prefix[-1] + n)
#         total = prefix[-1] 
        
#         minn = float('inf')
#         output = None
#         div = lambda A, B: 0 if B == 0 else A // B #per question, the average of 0 elements is 0
#         for i in range(len(nums)):
#             A = prefix[i] // (i+1)
#             B = div(total - prefix[i], (len(nums) - (i+1)))
#             diff = abs(A-B) 
#             if diff < minn:
#                 minn = diff 
#                 output = i
#         return output
    
    
