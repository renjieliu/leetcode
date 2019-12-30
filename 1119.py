class Solution:
    def removeVowels(self, S: str) -> str:
        output = ""
        for c in S:
            if c not in ['a','e','i','o','u']:
                output+=c
        return output
