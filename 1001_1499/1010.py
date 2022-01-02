class Solution:
    def numPairsDivisibleBy60(self, time: 'List[int]') -> int:
        possible = {i for i in range(60, 1000, 60)} #all the possible total length, which could be divided by 60
        seen = set()
        # print(possible)
        cnt = 0 
        hmp = {}
        fact = lambda x: 1 if x <= 1 else x * fact(x-1)
        comb = lambda m,n: fact(m)//(fact(m-n) * fact(n))
        for t in time:
            if t not in hmp:
                hmp[t] = 0 
            hmp[t] += 1 
        
        for k, v in hmp.items():
            for total in possible:
                A = min(k, total-k)
                B = max(k, total-k)
                if total - k in hmp and (A, B) not in seen :# if current combination was not seen before
                    seen.add((A, B)) 
                    if k == total-k:
                        cnt += comb(hmp[k], 2)
                    else:
                        cnt += hmp[k] * hmp[total-k]
                        
        return cnt 

    
# previous approach
# class Solution:
#     def numPairsDivisibleBy60(self, time: 'List[int]') -> int:
#         arr = [_ % 60 for _ in time]
#         hmp = {} # each remainder is a stack, to check if the number can find a match in the hashmap
#         for i in range(len(arr)):
#             a = arr[i]
#             if a not in hmp:
#                 hmp[a] = []
#             hmp[a].append(i)

#         cnt = 0

#         for i, a in enumerate(arr):
#             rem = (60 - a) % 60
#             if rem in hmp:
#                 while hmp[rem] and hmp[rem][0] <= i:#pop the stack, until the position is > the current
#                     hmp[rem].pop(0)
#                 cnt += len(hmp[rem])
#             # print(hmp)
#         return cnt
