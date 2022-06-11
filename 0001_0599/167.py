class Solution:
    def twoSum(self, numbers: 'List[int]', target: int) -> 'List[int]': #O( N | 1 )
        left = 0
        right = len(numbers)-1 
        while left < right: 
            if numbers[left] + numbers[right] == target:
                return [left+1, right+1] # the answer needs to be 1-indexed
            elif numbers[left] + numbers[right] < target: # if current sum is too big, move the right pointer
                left += 1
            else: # too small, then move the left pointer
                right -= 1
        



# previous solution

# class Solution:
#     def twoSum(self, numbers: 'List[int]', target: int) -> 'List[int]': #O(nlogn |  1)
#         def binFind(arr, s, v): #binary search for v, in arr, starting from s
#             e = len(arr)-1
#             while s <= e :
#                 mid = s - (s-e)//2
#                 if arr[mid] == v:
#                     return mid
#                 elif arr[mid] < v:
#                     s = mid + 1
#                 else:
#                     e = mid - 1
#             return -1 
        
#         for i in range(len(numbers)):
#             t = binFind(numbers, i+1, target - numbers[i]) #starting from i+1 position
#             if t != -1:
#                 return [i+1, t+1]  # the answer should be 1-indexed




# previous solution

# def twoSum(numbers, target):
#     """
#     :type numbers: List[int]
#     :type target: int
#     :rtype: List[int]
#     Input: numbers = [2,7,8,9,11,15,19,22], target = 9
#     Output: [1,2]
#     Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
#      -->> You may assume that each input would have exactly one solution and you may not use the same element twice.
#     """

#     map = {}
#     for i in range(0, len(numbers)):
#         if numbers[i] in map:
#             return [map[numbers[i]]+1, i+1]
#         else:
#             map[target-numbers[i]] = i

#     return map

# print(twoSum([2,7,8,9,11,15,19,22], 9 ))

