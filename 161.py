class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs(len(s) - len(t)) > 1:
            return False
        elif abs(len(s) - len(t)) == 1:  # if diff is 1, go thru the string, and compare each position.
            short = s if len(s) < len(t) else t
            long = t if short == s else s
            diff = 0
            while short and long:
                if short[0] == long[0]:
                    short = short[1:]
                    long = long[1:]
                else:
                    diff += 1
                    long = long[1:]
            return True if diff <= 1 else False  # if diff = 0, meaning the short is exausted and the last char mismatches.  if diff==1: satisfy the problem

        elif len(s) == len(t):  # go thru the string, and compare each position.
            diff = 0
            while s:
                if s[0] != t[0]:
                    diff += 1
                s = s[1:]
                t = t[1:]
            return True if diff == 1 else False
