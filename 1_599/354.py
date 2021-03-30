class Solution:
    def maxEnvelopes(self, arr: 'List[List[int]]') -> int:
        arr.sort(key = lambda x: x[1], reverse = True)
        arr.sort(key = lambda x: x[0])
        def bin_find(arr, v): #to find the point where all the numbers are > than the v
            if arr==[]:
                return 0
            elif v > arr[-1] :
                return len(arr)
            elif v < arr[0]:
                return 0
            else:
                s = 0
                e = len(arr)-1
                while s <= e:
                    mid = (s+e)//2
                    if arr[mid] >= v:
                        e-=1
                    else:
                        s+=1
                return s

        def helper(nums): #same logic as Longest increasing subsequence [6,3,2,1,3,4,5].
            dp = []
            for i in range(len(nums)):
                idx = bin_find(dp, nums[i])
                if idx == len(dp): #if larger than anything
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i] #replace the current arr element
            return len(dp)

        t = helper([a[1] for a in arr]) #only need to find the longest subseq of the second element
        return t


