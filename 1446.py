class Solution:
    def maxPower(self, s: str) -> int:
        if s == "":
            return 0
        output = 1
        curr = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                curr = 1

            output = max(curr, output)

        return output