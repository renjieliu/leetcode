class Solution:
    def findOriginalArray(self, changed: 'List[int]') -> 'List[int]': # O( NlogN | N )
        if len(changed) % 2 :
            return []
        hmp = {}
        for c in changed:
            if c not in hmp:
                hmp[c] = 0
            hmp[c] += 1 
        output = []
        taken = set()
        nums = sorted(hmp.keys(),reverse = True)  
        for n in nums: # check each even number, to see if it's taken.
            if n not in taken:
                if n == 0:
                    if hmp[0] % 2:
                        return []
                    else:
                        output += [0] * (hmp[0] // 2)
                elif n % 2 or n // 2 not in hmp or hmp[n//2] < hmp[n]: #if it's odd, it should be taken in the previous run.
                    return []
                else:
                    output += [n//2] * hmp[n]
                    hmp[n//2] -= hmp[n] 
                    if hmp[n//2] == 0: #it won't be checked again
                        taken.add(n//2)
        return output


                        
                        
                        
                        
                        
                        
# previous solution

# class Solution:
#     def findOriginalArray(self, changed: 'List[int]') -> 'List[int]':
#         if len(changed) % 2 == 1 :
#             return []
#         else:
#             changed.sort()
#             hmp = {} #counter for the original arr
#             double = {} #record the doubled number of curr
#             for c in changed:
#                 if c not in hmp:
#                     hmp[c] = 0
#                 hmp[c] += 1

#             output = []
#             for c in changed:
#                 if c in double: #itself if a double of some prev number
#                     double[c] -= 1
#                     if double[c] == 0:
#                         del double[c]
#                 elif c*2 in hmp: #check if doubled is in the hmp
#                     if c*2 not in double:
#                         double[c*2] = 0
#                     double[c*2] += 1
#                     output.append(c)
#                 else: #not as doubled of some number, and doubled self not in arr
#                     return []
#             return output if double == {} else [] # double need to be cleared.



