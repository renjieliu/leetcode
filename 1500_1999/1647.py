class Solution:
    def minDeletions(self, s: str) -> int: #O( NlogN | K ), K is the unique letters in s, worst case is 26.
        arr = [0] * 26
        for c in s :
            arr[ord(c) - ord('a')] += 1
        arr = sorted([a for a in arr if a != 0], reverse = True) # sort the occurrence in reverse order
        
        if len(arr) == 1:
            return 0 
        else:
            cnt = 0
            dp = [arr[0]] 
            for a in arr[1:]: 
                if dp[-1] <= 1:
                    cnt += a
                    dp.append(0)
                else:
                    if a >= dp[-1]: # current added need to be less than the previous added.
                        cnt += abs(dp[-1]-1-a) # add the difference to the cnt
                        dp.append(dp[-1]-1)
                    else: # already smaller than the previous one, no need to change
                        dp.append(a) 
            return cnt
                    
            
# previous solution

# class Solution:
#     def minDeletions(self, s: str) -> int:
#         if len(s) == 1:  return 0
#         hmp = {}
#         for c in s:
#             if c not in hmp:
#                 hmp[c] = 0
#             hmp[c] += 1
#         lkp = {}
#         for k, v in hmp.items():
#             if v not in lkp:
#                 lkp[v] = []
#             lkp[v].append(k)
#         # print(lkp)
#         lst = list(lkp.keys())
#         output = 0
#         for l in lst:
#             if len(lkp[l]) > 1:
#                 for c in lkp[l][1:]:
#                     find = 0
#                     for i in range(l, -1, -1):
#                         if i not in lkp:
#                             lkp[i] = None
#                             find = i
#                             break
#                     output += (l - find)

#         return output
