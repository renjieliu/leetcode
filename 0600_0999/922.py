class Solution:
    def sortArrayByParityII(self, nums: 'List[int]') -> 'List[int]':
        odd = 1
        for even in range(0, len(nums), 2): #swap within the array itself.
            if nums[even] %2 : # even location, odd number, need to swap
                while nums[odd] % 2: #odd locatio, odd number, need to pass
                    odd+=2
                nums[even], nums[odd] = nums[odd], nums[even]
        return nums



# previous approach
# class Solution:
#     def sortArrayByParityII(self, nums: 'List[int]') -> 'List[int]':
#         output = [None for _ in range(len(nums))]
#         even = 0
#         odd = 1
#         for i in range(len(nums)):
#             curr = nums[i]
#             if curr % 2 == 1:
#                 output[odd] = curr
#                 odd += 2
#             else:
#                 output[even] = curr
#                 even += 2
#         return output
#



# previous approach
# def sortArrayByParityII(A: 'List[int]'):
#     output = [None] * len(A)
#     curr_odd = 1
#     curr_even = 0
#     for i in A:
#         if i&1==0:
#             output[curr_even] = i
#             curr_even+=2
#         else:
#             output[curr_odd] = i
#             curr_odd += 2
#
#     return output
#
#
#     #
#     #
#     # odd = []
#     # even = []
#     # output =[]
#     # for i in A :
#     #     if i &1==0:
#     #         even.append(i)
#     #     else:
#     #         odd.append(i)
#     # for i in range(len(A)):
#     #     if i &1==0:
#     #         output.append(even.pop())
#     #     else:
#     #         output.append(odd.pop())
#     #
#     # return output
#     #
#

# print(sortArrayByParityII([4,2,5,7]))
