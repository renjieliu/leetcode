class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        output = 0 
        for i in range(len(word)):
            for j in range(i+1, len(word)):
                output += (set(word[i:j+1]) == set('aeiou'))
        return output

    