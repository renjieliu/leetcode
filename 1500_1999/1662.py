class Solution:
    def arrayStringsAreEqual(self, word1: 'List[str]', word2: 'List[str]') -> bool: # O( N | 1 )
        return ''.join(word1) == ''.join(word2)
    

# previous solution 

# class Solution:
#     def arrayStringsAreEqual(self, word1: 'List[str]', word2: 'List[str]') -> bool:
#         return ''.join(word1) == ''.join(word2)




# previous solution

# class Solution:
#     def arrayStringsAreEqual(self, word1: 'List[str]', word2: 'List[str]') -> bool:
#         return "".join(word1)=="".join(word2)

