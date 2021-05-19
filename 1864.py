class Solution:
    def minSwaps(self, s: str) -> int:
        zero = s.count("0")
        one = s.count("1")
        if abs(zero - one) > 1:
            return -1
        else: #construct the target string, a and b
            a = "1"
            while len(a) < len(s):
                a += "0" if a[-1] == "1" else "1"
            b = "0"
            while len(b) < len(s):
                b += "1" if b[-1] == "0" else "0"
            cnt_a = cnt_b = 0
            for i in range(len(s)): #check the difference for all the positions, for both 2 target
                cnt_a += 1 if s[i] != a[i] else 0
                cnt_b += 1 if s[i] != b[i] else 0

            if zero == one: # even length, turn the s into a and b, the swap is the total diff //2
                return min(cnt_a//2, cnt_b//2)
            elif zero > one: # the result should be 10101...
                return cnt_b//2
            else: # the target should be 0101010...
                return cnt_a//2







