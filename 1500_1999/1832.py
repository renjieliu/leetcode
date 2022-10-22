class Solution:
    def checkIfPangram(self, sentence: str) -> bool: # O( N | 26 )
        return len(set(sentence)) == 26

    

# previous solution

# class Solution:
#     def checkIfPangram(self, sentence: str) -> bool:
#         return len(set(sentence))==26


