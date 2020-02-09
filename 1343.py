class Solution:
    def numOfSubarrays(self, arr: 'List[int]', k: int, threshold: int) -> int:
        dp = []
        i = 0
        s = 0
        cnt = 0
        while i < len(arr):
            s+=arr[i]
            dp.append(s)
            if len(dp) == k:
                if dp[-1] >= threshold*k:
                    cnt +=1
            elif len(dp) > k:
                if dp[-1] - dp[-k-1] >= threshold*k: #get the diff in between
                    cnt +=1
            i+=1
        return cnt