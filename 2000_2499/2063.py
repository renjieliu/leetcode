class Solution:
    def countVowels(self, word: str) -> int: #for each vowel, it can appear in (i+1)*(total-i) substring
        n = len(word)
        return sum( (i+1)*(n-i) for i, w in enumerate(word) if w in 'aeiou')
        
        
        
# class Solution:
#     def countVowels(self, word: str) -> int: # dp
#         prev = 1 if word[0] in 'aeiou' else 0
#         total = prev
#         for i in range(1, len(word)): 
#             if word[i] in 'aeiou': # assuming the string ends here + itself
#                 prev = prev + i + 1
#             total += prev
#         return total

    
    