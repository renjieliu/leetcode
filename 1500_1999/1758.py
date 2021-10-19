class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) == 1:
            return 0
        else:
            t1 = "0"
            t2 = "1"
            for i in range(1, len(s)):  # constuct 2 target string, 101010...., 01010101...
                t1 += "1" if t1[-1] == "0" else "0"
                t2 += "1" if t2[-1] == "0" else "0"

            cnt_1 = cnt_2 = 0
            for i in range(len(s)):  # comparen with the target string and see the changes
                if s[i] != t1[i]:
                    cnt_1 += 1
                if s[i] != t2[i]:
                    cnt_2 += 1

            return min(cnt_1, cnt_2)


