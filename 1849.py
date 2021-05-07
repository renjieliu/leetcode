class Solution:
    def splitString(self, s: str) -> bool:
        def helper(pool, num, arr):
            if len(arr) == 0 and len(pool) > 1: #it can be split to 2 or more strings
                return 1
            elif num == 0: #if the last number is 0, check the rest, they should be all 0
                if sum([int(_) for _ in arr]) == 0:
                    return 1
                else:
                    return 0
            else:
                curr = "0"
                while arr: #keep adding numbers, until it's num-1
                    curr += arr.pop(0)
                    if int(curr) == num-1:
                        pool.append(int(curr))
                        if helper(pool, int(curr), arr) == 1 :
                            return 1
                    elif int(curr) > num:
                        return 0
                return 0

        s = s.lstrip('0') #take out the leading 0 from the original string
        if len(s) <= 1 :
            return False
        for i in range(len(s)//2+1):
            t = helper([int(s[:i+1])], int(s[:i+1]), list(s[i+1:]))
            if t == 1:
                return True
        return False




