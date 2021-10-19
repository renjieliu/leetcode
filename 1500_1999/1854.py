class Solution:
    def maximumPopulation(self, logs: 'List[List[int]]') -> int:  # using the range addition approach
        start = float('inf')
        end = -float('inf')
        for a, b in logs:
            start = min(start, a)
            end = max(end, b)
        arr = [0] * ((end - start) + 1)
        for a, b in logs:
            arr[a - start] += 1
            arr[b - start] -= 1
        v = arr[0]
        for i in range(1, len(arr)):
            arr[i] += arr[i - 1]
            v = max(v, arr[i])
        for i, a in enumerate(arr):
            if a == v:
                return i + start


# previous approach
# class Solution:
#     def maximumPopulation(self, logs: 'List[List[int]]') -> int:
#         hmp = {}
#         for a, b in logs:
#             for i in range(a,b):
#                 if i not in hmp:
#                     hmp[i] = 0
#                 hmp[i]+=1
#         v = max(hmp.values())
#         for k in sorted(list(hmp.keys())):
#             if hmp[k] == v:
#                 return k

