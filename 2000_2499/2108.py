class Solution:
    def firstPalindrome(self, words: 'List[str]') -> str:
        return ([w for w in words if w==w[::-1]] + [""])[0] # padding "" to the end of the arr, in case empty

