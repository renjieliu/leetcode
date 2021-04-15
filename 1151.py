class Solution:
    def minSwaps(self, data: 'List[int]') -> int:
        s = sum(data)
        if s<=1 or s == len(data):
            return 0
        else:#how many 0's if to move everything here
            arr = [sum(data[:s])]
            for i in range(s, len(data)):
                arr.append(arr[-1] - data[i-s] + data[i])
            res = float('inf')
            for a in arr :
                res = min(s-a, res)
            return res


# previous approach
# class Solution:
#     def minSwaps(self, data: 'List[int]') -> int:
#         sum_dp = []
#         s = 0
#         for i in range(len(data)):
#             s+=data[i]
#             sum_dp.append(s)
#         s = sum_dp[-1]
#         i = 0
#         output = len(data) - s #how many 0 are in the array, max swap will be this amount
#         while i < len(data) - s + 1:
#             #curr = data[i:i+s] #each time, put the window as current to current + s
#             curr_sum = sum_dp[i+s-1] - (0 if i ==0 else sum_dp[i-1])
#             #print(curr)
#             output = min(s-curr_sum, output) #for current windows, find how many 0 are there. 0's will be swaped
#             i+=1
#         return output