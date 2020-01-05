class Solution:
    def xorQueries(self, arr: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        dp = [0]
        t = arr[0]
        for i in range(1, len(arr)):
            t^=arr[i]
            dp.append(t)

        output = []
        for q in queries:
            if q[0] ==q[1]:
                output.append( arr[q[0]] )
            elif q[0] == 0:
                output.append(dp[ q[1] ])
            else:
                output.append( dp[q[1]] ^ dp[q[0]] ^ arr[q[0]] ) #avoid xor dp[0], subtract the full segment from the whole, and xor the head
        return output
