class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0 
        for c in s+t: #all the character should be duplicated, except for the additional one.
            xor ^= ord(c)
        return chr(xor)

#         arr = [0 for _ in range(26)] # record the frequency of each character
#         for i, c in enumerate(s):
#             arr[ord(c) - ord('a')] += 1
#             arr[ord(t[i]) - ord('a')] -=1 
        
#         arr[ord(t[-1]) - ord('a')] -=1 #since t has one more character than s, need to record the last character of t
        
#         for i in range(len(arr)):
#             if arr[i] != 0: #if they are same, all the number in arr should be 0.
#                 return chr(i+ord('a'))
            
            


# previous approach

# class Solution:
#     def findTheDifference(self, s: str, t: str) -> str:
#         hmp_s = {}
#         hmp_t = {} 
#         for c in s:
#             if c not in hmp_s:
#                 hmp_s[c] = 0
#             hmp_s[c] +=1 
#         for c in t:
#             if c not in hmp_t:
#                 hmp_t[c] = 0
#             hmp_t[c] += 1 
        
#         for k, v in hmp_t.items():
#             if k not in hmp_s or hmp_s[k] < hmp_t[k]:
#                 return k
            
        


# previous approach

# def findTheDifference(s, t):
#     """
#     :type s: str
#     :type t: str
#     :rtype: str
#     """
#     sum_s = 0
#     for i in list(s):
#         sum_s += ord(i)

#     sum_t=0
#     for i in list(t):
#         sum_t += ord(i)

#     return chr(sum_t - sum_s)

# print(findTheDifference("abcd", "abcde"))





