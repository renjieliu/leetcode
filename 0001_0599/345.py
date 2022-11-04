class Solution:
    def reverseVowels(self, s: str) -> str: # O( N | N )
        s = list(s)
        l = 0 
        r = len(s)-1 
        while l <= r: # check vowels from start
            if s[l].lower() in "aeiou": # meet vowel
                while r >= l: # searching for the counterpart from the end, and swap
                    if s[r].lower() in "aeiou":
                        s[l], s[r] = s[r], s[l] #swap s[l] and s[r]
                        r-=1 # move the right pointer after swap
                        break
                    r -= 1 
            l += 1 # advance the left pointer
        
        return "".join(s)



# previous solution

# class Solution:
#     def reverseVowels(self, s: str) -> str: # O( N | N )
#         loc = [] # record all the vowel location
        
#         for i, c in enumerate(s):
#             if c.lower() in "aeiou":
#                 loc.append(i)
#         output = ""
        
#         for i, c in enumerate(s): # find the corresponding vowel from the end
#             if c.lower() in "aeiou":
#                 output += s[loc.pop()]
#             else:
#                 output += c
        
#         return output



# previous solution 

# def reverseVowels(s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     temp = []
#     vowel = ['a','A','e','E','i','I','o','O','u','U']
#     for i in range(0, len(s)):
#         if s[i] in vowel:
#             temp.append(s[i])
#     output=""
#     cnt = -1
#     for i in range(0, len(s)):
#         if s[i] in vowel:
#             output+= temp[cnt]
#             cnt -= 1
#         else:
#             output+= s[i]

#     return output

# print(reverseVowels("hello"))
# print(reverseVowels("leetcode"))


