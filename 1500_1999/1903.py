class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = {"1","3","5","7","9"} #lookup is faster than int(num[i])%2 == 1 approach
        for i in range(len(num)-1, -1, -1):
            if num[i] in odd:
                return num[:i+1]
        return ""


