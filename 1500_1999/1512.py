class Solution:
    def numIdenticalPairs(self, nums: 'List[int]') -> int:
        cnt = 0
        hmp = {}
        for n in nums:  # O(N), to check how many times the number appeared before.
            if n in hmp:
                hmp[n] += 1
                cnt += hmp[n]
            else:
                hmp[n] = 0  # it's the new number, set the counter to 0
        return cnt

# old approach: O(N2)
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[j] == nums[i]:
#                     cnt +=1
#         return cnt
