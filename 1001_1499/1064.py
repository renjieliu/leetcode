class Solution:
    def fixedPoint(self, arr: 'List[int]') -> int: #binary search, O(NlogN)
        s = 0 
        e = len(arr)-1
        output = float('inf')
        while s <= e:
            mid = s-(s-e)//2
            if arr[mid] >= mid: #arr is sorted, if arr[idx] > idx, the arr[idx]==idx should be on the left
                output = min(output, mid) if arr[mid] == mid else output
                e = mid - 1
            else:
                s = mid + 1
        return output if output!=float('inf') else -1
        
        
        
#         for i, c in enumerate(arr):
#             if i == c :
#                 return c
#         return -1





# previous approach

# class Solution:
#     def fixedPoint(self, A: 'List[int]') -> int:
#         for i in range(len(A)) :
#             if A[i] ==i:
#                 return i
#         return -1


