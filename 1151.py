class Solution:
    def minSwaps(self, data: 'List[int]') -> int:
        sum_dp = []
        s = 0
        for i in range(len(data)):
            s+=data[i]
            sum_dp.append(s)
        s = sum_dp[-1]
        i = 0
        output = len(data) - s #how many 0 are in the array, max swap will be this amount
        while i < len(data) - s + 1:
            curr_sum = sum_dp[i+s-1] - (0 if i ==0 else sum_dp[i-1])
            output = min(s-curr_sum, output) #for current windows, find how many 0 are there. 0's will be swaped
            i+=1
        return output