class Solution:
    def vowelStrings(self, words: 'List[str]', left: int, right: int) -> int: # O( N | 1 )
        cnt = 0 
        for i, w in enumerate(words): # go through each word, to check if it's a vowel string
            cnt += 1 if left <= i <= right and w[0] in "aeiou" and w[-1] in "aeiou" else 0
        return cnt

