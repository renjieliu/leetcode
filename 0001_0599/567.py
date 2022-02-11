class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: #O(len(L1) + 26*(L2-L1)) ==> O(26N) ==> O(N)
        a1 = [0]*26 #record the occurrence of each character
        a2 = [0]*26
        for c in s1: 
            a1[ord(c) - ord('a')] += 1
        
        for i in range(len(s2)):
            if i >= len(s1):
                a2[ ord(s2[i-len(s1)]) - ord('a') ] -= 1 #take out the previous character
            
            a2[ord(s2[i]) - ord('a')] += 1 
            
            if a2==a1: #compare a1 and a2. 
                return True
        
        return False
    
    



# previous approach

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         def sameHash(h1, h2):
#             if len(h1) != len(h2):
#                 return False
#             for k, v in h1.items():
#                 if k not in h2 or h2[k] != v:
#                     return False
#             return True

#         if s1 == "":
#             return True if s2 != "" else False
#         lkp = {}
#         for c in s1:
#             if c not in lkp:
#                 lkp[c] = 0
#             lkp[c] += 1
#         left = 0
#         curr = {}
#         for right in range(len(s2)):
#             if s2[right] not in curr:
#                 curr[s2[right]] = 0
#             curr[s2[right]] += 1

#             if right - left + 1 == len(s1):
#                 if sameHash(lkp, curr):
#                     return True
#                 else:
#                     curr[s2[left]] -= 1
#                     if curr[s2[left]] == 0:
#                         del curr[s2[left]]
#                     left += 1

#         return False


# previous approach 

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         def compareDict(d1, d2):
#             if set(d1.keys()) - set(d2.keys()) == set():
#                 for i in d1.keys():
#                     if d1[i] != d2[i]:
#                         return False
#                 return True
#             else:
#                 return False


#         if len(s2) < len(s1):
#             return False
#         lkp = {}
#         for i in s1:
#             if i not in lkp:
#                 lkp[i] =0
#             lkp[i] += 1
#         dict = {}

#         for i in range(len(s1)):
#             if s2[i] not in dict:
#                 dict[s2[i]] = 0
#             dict[s2[i]] += 1
#         if compareDict(lkp, dict) == True:
#             return True
#         else:
#             for i in range(len(s1), len(s2)):
#                 rm = i-len(s1)
#                 c = s2[rm]
#                 if dict[c] == 1:
#                     del dict[c]
#                 else:
#                     dict[c] -=1

#                 if s2[i] not in dict:
#                     dict[s2[i]] = 0
#                 dict[s2[i]] += 1

#                 if compareDict(lkp, dict) ==True:
#                     return True

#         return False



