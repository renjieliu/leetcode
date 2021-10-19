class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        nums.sort()
        output = []
        i = 0
        while i < len(nums)-2:
            curr = nums[i]
            j, k = i+1, len(nums)-1
            while j < k:
                t = nums[j] + nums[k]
                if t > -curr:
                    k-=1
                elif t < -curr:
                    j+=1
                elif t == -curr:
                    output.append([curr, nums[j] , nums[k] ]  )
                    cj = nums[j]
                    ck = nums[k]
                    while j< k and nums[j] == cj:
                        j+=1
                    while j< k and nums[k] == ck:
                        k-=1
            ci = nums[i]
            while i < len(nums)-2 and nums[i]==ci:
                i+=1
        return output