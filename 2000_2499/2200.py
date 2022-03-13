class Solution:
    def findKDistantIndices(self, nums: 'List[int]', key: int, k: int) -> 'List[int]': #O(n2)
        arr = [i for i, n in enumerate(nums) if n == key] # find all the index with key
        output = []
        for i in range(len(nums)): #check one by one to see if it can satisfy the condition
            if arr:
                if abs(arr[0]-i) <= k:
                    output.append(i)
                else:
                    while arr and arr[0] < i and abs(arr[0]-i) > k: # take out the smaller index from arr , or distant > k 
                        arr.pop(0)
                    if arr and abs(arr[0]-i) <= k:
                        output.append(i)
        return output

    


# previous approach 

# class Solution:
#     def findKDistantIndices(self, nums: 'List[int]', key: int, k: int) -> 'List[int]': #O(n2)
#         arr = [i for i, n in enumerate(nums) if n == key] # find all the index with key
#         output = []
#         for i in range(len(nums)): #check one by one to see if it can satisfy the condition
#             for a in arr:
#                 if abs(a-i) <=k:
#                     output.append(i)
#                     break 
#         return output

    
    
    
