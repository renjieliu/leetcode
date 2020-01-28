class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        i = 0
        while i < len(palindrome):
            t = palindrome[:i] + 'a' + palindrome[i + 1:]  # replace current to 'a'
            if t != t[::-1]:  # still palindrome, need to continue
                return t
            i += 1
        return palindrome[:-1] + 'b'


