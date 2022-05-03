class Solution:
    def sortArrayByParity(self, nums: 'List[int]') -> 'List[int]': #O(N | 1)
        r = len(nums)-1 
        l = 0 
        while l <= r :
            if nums[l] % 2: 
                while l < r and nums[r] % 2: #find the first even number from right
                    r-=1 
                if l < r:
                    nums[l], nums[r] = nums[r], nums[l] #swap the number
            l += 1
        return nums



# previous solution

# class Solution:
#     def sortArrayByParity(self, nums: 'List[int]') -> 'List[int]': # O(N | N)
#         return [_ for _ in nums if _%2 == 0] + [_ for _ in nums if _%2]


# previous solution

# class Solution:
#     def sortArrayByParity(self, A: 'List[int]') -> 'List[int]':
#         odd = []
#         even = [] 
#         for a in A:
#             if a%2:
#                 odd.append(a)
#             else:
#                 even.append(a)
#         return even+odd

# previous solution

# def sortArrayByParity(A: 'List[int]'):
#     output1 = []
#     output2 = []
#     for i in A:
#         if int(i) % 2 == 0:
#             output1.append(i)
#         else:
#             output2.append(i)
#     return output1 + output2

# print(sortArrayByParity([3,1,2,4]))