class Solution:
    def halvesAreAlike(self, s: str) -> bool: # O( N | 1 )
        A = B = 0 
        for i in range(len(s)): #for each character, check if it's vowel, and assign to first and second half
            if i < len(s)//2:
                A += s[i].upper() in "AEIOU"
            else:
                B += s[i].upper() in "AEIOU"
        
        return A == B


# previous solution

# class Solution:
#     def halvesAreAlike(self, s: str) -> bool:
#         left = 0
#         right = len(s)-1
#         a = b = 0
#         lkp = set("aeiouAEIOU")
#         while left <= right: #the length of s is even, left + 1 and right -1 each time. no overlap happens
#             if s[left] in lkp:
#                 a += 1
#             if s[right] in lkp:
#                 b += 1
#             left +=1
#             right -= 1
#         return a==b
