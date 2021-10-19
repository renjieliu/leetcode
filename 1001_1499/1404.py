class Solution:
    def numSteps(self, s: str) -> int:
        def binToDec(s):
            power = 0
            output = 0
            for c in s[::-1]:
                output += int(c) * (2 ** power)
                power += 1
            return output

        t = binToDec(s)
        cnt = 0
        while t != 1:
            if t % 2 == 0:
                t = t // 2
            else:
                t += 1
            cnt += 1
        return cnt