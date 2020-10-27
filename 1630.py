class Solution:
    def checkArithmeticSubarrays(self, nums: 'List[int]', l: 'List[int]', r: 'List[int]') -> 'List[bool]':
        def isArithmetic(arr):
            if len(arr) == 1 :
                return True
            else:
                diff = arr[1] - arr[0]
                for i in range(1, len(arr)) :
                    if arr[i] - arr[i-1] != diff:
                        return False
                return True
        output = []
        for i in range(len(l)):
            check = sorted(nums[l[i]: r[i]+1]) #check if the sorted target arr is Arithmetic
            output.append(isArithmetic(check))
        return output