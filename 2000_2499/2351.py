class Solution:
    def repeatedCharacter(self, s: str) -> str: # O( N | 26)
        arr = [0]*26 #slot for each lower case English letter
        for c in s:
            idx = ord(c)-ord('a')
            arr[idx] += 1 
            if arr[idx] == 2:
                return c
            


# previous solution 

# class Solution:
#     def repeatedCharacter(self, s: str) -> str: # O( N | 26)
#         arr = [0]*26 #slot for each lower case English letter
#         for c in s:
#             idx = ord(c)-ord('a')
#             arr[idx] += 1 
#             if arr[idx] == 2:
#                 return c
            
