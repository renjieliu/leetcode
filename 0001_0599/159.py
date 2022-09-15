class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int: # O( N | N )
        l = r = 0 
        lkp = {}
        output = 0
        while r < len(s): # go through the string, using 2 pointers to check how many distinct letters in between
            if s[r] not in lkp:
                while l < r and len(lkp) == 2: #if there're 2 distinct letters, keep pushing the left pointer
                    lkp[s[l]] -= 1
                    if lkp[s[l]] == 0 :
                        del lkp[s[l]]
                    l += 1
                lkp[s[r]] = 0 # initiate to be 0
                
            lkp[s[r]] += 1 # if it's in the lkp, just add one more.
            output = max(output, r-l+1)
            r += 1 
        return output

    
                
            

# previous solution

# class Solution:
#     def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
#         hmp = {}
#         start_loc = 0
#         output = 0
#         for i, c in enumerate(s):  # eceba
#             if c not in hmp:
#                 if len(hmp) == 2:
#                     lst = list(hmp.keys())
#                     if hmp[lst[0]][-1] < hmp[lst[1]][-1]:  # remove the one ends first, and get the new start_loc
#                         t = hmp[lst[0]][-1]
#                         del hmp[lst[0]]
#                         while hmp[lst[1]][0] < t:
#                             hmp[lst[1]].pop(0)
#                         start_loc = hmp[lst[1]][0]
#                     else:
#                         t = hmp[lst[1]][-1]
#                         del hmp[lst[1]]
#                         while hmp[lst[0]][0] < t:
#                             hmp[lst[0]].pop(0)
#                         start_loc = hmp[lst[0]][0]

#                     hmp[c] = [i]
#                     output = max(output, (i - start_loc) + 1)
#                 else:
#                     hmp[c] = [i]
#                     output = max(output, (i - start_loc) + 1)
#             else:
#                 hmp[c].append(i)
#                 output = max(output, (i - start_loc) + 1)

#             # print(hmp, c, output)

#         return output




