class Solution:
    def minOperations(self, nums: 'List[int]', x: int) -> int:
        right = {0:len(nums)} # sum and the index
        output = float('inf')
        s = 0
        a = nums[::-1] #check sum from right end
        for i, n in enumerate(a):
            s+=a[i]
            right[s] = len(a)-1-i

        output = (len(nums)- right[x]) if x in right else float('inf')

        s = 0
        for i, n in enumerate(nums): # to see if x-currsum exists on the right side
            s+=nums[i]
            if x-s in right:
                if right[x-s] > i:
                    leftOperation = i+1
                    rightOperation= len(nums)-right[x-s]
                    output = min(output, leftOperation+rightOperation )
        return output if output!=float('inf') else -1









