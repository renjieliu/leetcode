class Solution:
    def answerQueries(self, nums: 'List[int]', queries: 'List[int]') -> 'List[int]': # O( NlogN | N )
        nums.sort()
        arr = [nums[0]]
        for n in nums[1:]: # to calc the prefix sum
            arr.append(arr[-1] + n)
        
        def binFind(arr, v): # to find how many elements in arr <= v:
            if v >= arr[-1]:
                return len(arr)
            elif v < arr[0]:
                return 0 
            else:
                s = 0 
                e = len(arr)-1 
                output = -1
                while s <= e:
                    mid = s - (s-e)//2 
                    if arr[mid] <= v:
                        s = mid + 1
                        output = mid
                    else:
                        e = mid - 1
                return output + 1 
        
        return [binFind(arr, q) for q in queries] # for each query, find how many in the prefix sum is <= q


    




# previous solution

# class Solution:
#     def answerQueries(self, nums: 'List[int]', queries: 'List[int]') -> 'List[int]': # O( NlogN | N )
#         pre = [0]
#         for n in sorted(nums): # prefix sum for the sorted(nums)
#             pre.append(pre[-1] + n)
#         pre.pop(0)
        
#         def binFind(arr, v): # find the last index in the arr, with value <= v 
#             s = 0 
#             e = len(arr)-1
#             output = 0
#             while s <= e:
#                 mid = s - (s-e) //2 
#                 if arr[mid] > v:
#                     e = mid - 1 
#                 else:
#                     s = mid + 1 
#             return s

#         return [binFind(pre, q) for q in queries] 
                    
