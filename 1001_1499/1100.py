class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k :
            return 0
        
        hmp = {}
        for i in range(k): #build the initial hashmap
            if s[i] not in hmp:
                hmp[s[i]] = 0
            hmp[s[i]] += 1
        
        output = 1 if len(hmp) == k else 0
        
        for i in range(k, len(s)): #go through the string, take out the prev, add curr, and see if it's unique
            prev = i - k
            hmp[s[prev]]-=1 
            if hmp[s[prev]] == 0 :
                del hmp[s[prev]]
            if s[i] not in hmp:
                hmp[s[i]] = 0 
            hmp[s[i]] += 1
        
            output += 1 if len(hmp) == k else 0 
        
        return output
    

    


# previous approach

# class Solution:
#     def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
#         if len(S) < K or K > 26: return 0
#         i = 0
#         cnt = 0
#         while i < len(S)+1-K:
#             t = S[i:i+K]
#             if len(t) == len(set(list(t))):
#                 cnt +=1
#             i+=1
#         return cnt


