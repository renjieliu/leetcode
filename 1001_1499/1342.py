class Solution:
    def numberOfSteps (self, num: int) -> int:
        cnt = 0
        while num!=0:
            if num %2 != 0 :
                num -= 1
                cnt += 1
                if num == 0 :
                    return cnt
            num = num >> 1
            cnt += 1
        return cnt



