class Solution:
    def topKFrequent(self, nums: 'List[int]', k: int) -> 'List[int]': # bucket sort, O(N | N)
        hmp = {}
        mx = 0
        for n in nums:
            if n not in hmp:
                hmp[n] = 0
            hmp[n] += 1 
            mx = max(hmp[n], mx)
        
        bucket = [[] for _ in range(mx)] #to record the number with index occurrence 
        
        for n, occ in hmp.items():
            bucket[occ-1].append(n)
        
        output = []
        for b in bucket[::-1]:
            output += b
            # print(output, len(output), k)
            if len(output) == k:
                return output
        


# previous solution

# class Solution:
#     def topKFrequent(self, nums: 'List[int]', k: int) -> 'List[int]': #O(N)
#         hmp = {}
#         for n in nums:
#             if n not in hmp:
#                 hmp[n] = 0
#             hmp[n] += 1
#         total = max(hmp.values()) + 1
#         arr = [[] for _ in range(total)]
#         for c, v in hmp.items():
#             arr[v].append(c)
#         output = []
#         for a in arr[::-1]:
#             if a:
#                 output += a
#                 if len(output) == k:
#                     return output
#         return output


#previous approach

# class Solution:
#     def topKFrequent(self, nums: 'List[int]', k: int) -> 'List[int]': #O(nlogn)
#         hmp = {}
#         for n in nums:
#             if n not in hmp:
#                 hmp[n] = 0
#             hmp[n]+=1
#         t = list(hmp.keys())
#         return sorted(t, key = lambda x : hmp[x], reverse = True)[:k]
