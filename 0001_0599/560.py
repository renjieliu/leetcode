class Solution:
    def subarraySum(self, nums: 'List[int]', k: int) -> int:
        hmp = {0:1} # {sum: count}
        curr = 0 #total sum up to now
        output = 0
        for i, n in enumerate(nums):
            curr += n 
            output += hmp[curr-k] if curr-k in hmp else 0 # meaning current segment total is 0.
            
            if curr not in hmp:
                hmp[curr] = 0
            hmp[curr] += 1
        
        return output




# previous approach

# class Solution:
#     def subarraySum(self, nums: 'List[int]', k: int) -> int:
#         hmp = {0:1} #have seen 0 once, curr sum
#         s = 0
#         cnt = 0
#         for n in nums:
#             s+=n
#             if s-k in hmp:
#                 cnt += hmp[s-k]
#             if s not in hmp:
#                 hmp[s] = 0
#             hmp[s] +=1
#         return cnt 


# previous approach

# class Solution:
#     def subarraySum(self, nums: 'List[int]', k: int) -> int:
#         hmp = {0:1}
#         output = 0
#         s = 0
#         for n in nums:
#             s+=n
#             if s-k in hmp:
#                 output+=hmp[s-k]
#             if s not in hmp:
#                 hmp[s] = 0
#             hmp[s]+=1
#         return output
