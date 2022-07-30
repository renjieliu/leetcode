class Solution:
    def isAnagram(self, s: str, t: str) -> bool: # O( N | 52 )
        if len(s) != len(t):
            return False
        arr_1 = [0] * 26 # record the occurrence of each letter
        arr_2 = [0] * 26
        for i, c in enumerate(s): 
            arr_1[ord(c) - ord('a')] += 1
            arr_2[ord(t[i]) - ord('a')] += 1
        return arr_1 == arr_2 # compare if the 2 arrays are same
    


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool: # O( N | N )
#         if len(s) != len(t): 
#             return False
#         hmp_a = {}  # using hashmap to solve the follow-up for the unicode cases
#         hmp_b = {}
#         for i in range(len(s)):
#             if s[i] not in hmp_a:
#                 hmp_a[s[i]] = 0
#             hmp_a[s[i]] += 1 
            
#             if t[i] not in hmp_b:
#                 hmp_b[t[i]] = 0 
#             hmp_b[t[i]] += 1 
            
#         for k, v in hmp_a.items():
#             if k not in hmp_b or hmp_b[k] != v:
#                 return False 
#         return True                
            
        
        
    
        
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool: # O( N | 52 ) 
#         arr_1 = [0] * 26 # record the occurrence of each letter
#         arr_2 = [0] * 26
#         for c in s: 
#             arr_1[ord(c) - ord('a')] += 1
#         for c in t:
#             arr_2[ord(c) - ord('a')] +=1
        
#         return arr_1 == arr_2 # compare if the 2 arrays are same
    
    
    



# previous solution 

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         hmp_s = defaultdict(int)
#         hmp_t = defaultdict(int)
#         for c in s:
#             hmp_s[c]+=1
#         for c in t:
#             hmp_t[c]+=1
#         return hmp_s==hmp_t

#         #return sorted(list(s)) == sorted(list(t))


# previous approach
# def isAnagram(s, t):
#     s1 = list(str(s))
#     t1 = list(str(t))
#
#     s1.sort()
#     t1.sort()
#
#     if len(s1) != len(t1):
#         return False
#     else:
#         output = True
#         for i in range(0, len(s1)):
#             if s1[i]!=t1[i]:
#                 output = False
#                 break
#     return output
#
#
# print(isAnagram("anagram", "nagaram"))
#
#
#
