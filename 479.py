'''
https://leetcode.com/problems/largest-palindrome-product/discuss/276101/Python3-Math-and-Non-math-solutions-with-detailed-explanation

**Math solution:**
Let Palindrome = X * Y, both have n digits, and assume they are very close to 10^n
Denote X = 10^n - i, Y = 10^n - j, with assumption: i*j < 10^n
Palindrome = upper*10^n + lower = (10^n - i)*(10^n - j) = (10^n-i-j)*10^n + i*j
therefore: upper = 10^n-i-j, lower = i*j
Let a = i + j, then lower = i*(a-i), upper = 10^n-a
Algorithm: we iterate a and search for an integer i
i^2 - a*i + lower = 0 => (i-a/2)^2 = 0.25*a^2 - lower
Given a start from 2, check if sqrt(a^2 - lower*4) is an integer, then return upper*10^n + lower
'''


class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        else:
            curr = 1
            while curr < 10 ** n:
                upper = 10 ** n - curr
                low = int(str(upper)[::-1])
                check = (curr ** 2 / 4) - low
                if check >= 0 and check ** 0.5 == int(check ** 0.5):  # sqrt of the check is an integer
                    return (upper * (10 ** n) + low) % 1337
                curr += 1
