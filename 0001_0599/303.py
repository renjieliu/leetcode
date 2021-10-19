class NumArray:

    def __init__(self, nums: 'List[int]'):
        self.arr = [0]
        for n in nums:
            self.arr.append(self.arr[-1] + n)

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right+1] - self.arr[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


# previous approach
# class NumArray:
#     def __init__(self, nums: 'List[int]'):
#         self.ss =  []
#         sum =0
#         for i in range(len(nums)):
#             sum+=nums[i]
#             self.ss.append(sum)
#
#     def sumRange(self, i: int, j: int):
#         if i ==0 :
#             return self.ss[j]
#         else:
#             return self.ss[j] - self.ss[i-1]
#
#
#
# A = NumArray([-2, 0, 3, -5, 2, -1])
# print(A.sumRange(0,2))
# print(A.sumRange(2,5))
# print(A.sumRange(0,5))