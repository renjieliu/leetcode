class Solution:
    def divide(self, dividend: int, divisor: int) -> int:  # a/b
        a = dividend
        b = divisor
        if abs(b) > abs(a) or b == 0: return 0
        sign = -1 if ((a > 0 and b < 0) or (a < 0 and b > 0)) else 1
        a = abs(a)
        b = abs(b)
        res = [b]
        multiplier = [1]
        while res[-1] < a:  # keep adding until meet the dividend
            res.append(res[-1] + res[-1])
            multiplier.append(multiplier[-1] + multiplier[-1])  # 2,4,8,16....

        while res[-1] > a and multiplier[-1] - multiplier[-2] > 1:  # binary search to get the closest number
            res.pop()
            nxt_base = res[-1]
            curr = b
            multiplier.pop()
            times_base = multiplier[-1]  # the output should be > than current times_base
            times = 1
            while res[-1] < a:
                res.append(nxt_base + curr)  # this is like b*3, b*5, b*9...
                multiplier.append(times_base + times)
                times += times
                curr += curr

        if res[-1] > a:
            multiplier.pop()

        output = multiplier[-1] if sign == 1 else -multiplier[-1]

        if output > (2 ** 31 - 1) or output < (-2 ** 31):
            return 2 ** 31 - 1
        else:
            return output


