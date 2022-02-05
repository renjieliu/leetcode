class Solution:
    def maxScoreIndices(self, nums: 'List[int]') -> 'List[int]':
        left = [0] #accu sum from left
        for n in nums:
            left.append(left[-1]+n)
        
        right = [0] # accu sum on right
        for n in nums[::-1]:
            right.append(right[-1]+n)
        right = right[::-1]
        hmp = {}
        for i in range(len(nums)+1):
            L = i - left[i] # 0 on the left, if divide here
            R = right[i] # 1 on the right, if divide here
            if L+R not in hmp:
                hmp[L+R] = []
            hmp[L+R].append(i)
        
        # print(hmp)
        mx = max(hmp.keys())
        for k, v in hmp.items():
            if k == mx:
                return v

