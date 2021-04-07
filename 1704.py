class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        a = b = 0
        lkp = set("aeiouAEIOU")
        while left <= right: #the length of s is even, left + 1 and right -1 each time. no overlap happens
            if s[left] in lkp:
                a += 1
            if s[right] in lkp:
                b += 1
            left +=1
            right -= 1
        return a==b
