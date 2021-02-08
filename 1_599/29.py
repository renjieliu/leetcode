class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if abs(divisor) > abs(dividend) or dividend == 0: return 0
        sign = -1 if ((dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        curr_arr = [divisor]
        times_arr = [1]
        while curr_arr[-1] < dividend:  # binary search to find the end
            curr_arr.append(curr_arr[-1] + curr_arr[-1])
            times_arr.append(times_arr[-1] + times_arr[-1])

        while curr_arr[-1] > dividend and times_arr[-1] - times_arr[-2] > 1:  # binary seach to get close to the output
            curr_arr.pop()
            curr_base = curr_arr[-1]
            curr = divisor
            times_arr.pop()
            times_base = times_arr[-1]
            times = 1
            while curr_arr[-1] < dividend:
                curr_arr.append(curr_base + curr)
                times_arr.append(times_base + times)
                times += times
                curr += curr

        if curr_arr[-1] > dividend:
            times_arr.pop()

        output = times_arr[-1] if sign == 1 else -times_arr[-1]

        if output > (2 ** 31 - 1) or output < (-2 ** 31):
            return 2 ** 31 - 1
        else:
            return output


