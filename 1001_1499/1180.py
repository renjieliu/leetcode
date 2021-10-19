class Solution:
    def countLetters(self, S: str) -> int:
        curr = S[0]
        cnt = 0
        output = 0
        for c in S:
            if c == curr:
                cnt += 1
            else:
                output += (1 + cnt) * cnt // 2  # if 3 consecutive, there'll be (1+3)*3//2 Substrings
                cnt = 1
                curr = c
        output += (1 + cnt) * cnt // 2
        return output
