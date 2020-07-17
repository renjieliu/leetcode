class Solution:
    def topKFrequent(self, nums: 'List[int]', k: int) -> 'List[int]': #O(N)
        hmp = {}
        for n in nums:
            if n not in hmp:
                hmp[n] = 0
            hmp[n] += 1
        total = max(hmp.values()) + 1
        arr = [[] for _ in range(total)]
        for c, v in hmp.items():
            arr[v].append(c)
        output = []
        for a in arr[::-1]:
            if a:
                output += a
                if len(output) == k:
                    return output
        return output


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
