class Solution:
    def smallestCommonElement(self, mat: 'List[List[int]]') -> int: # O( NlogN | 1 )
        def binFind(v, arr): # to find v in arr with binary search
            if v < arr[0] or v > arr[-1]:
                return 0 
            else:
                s = 0 
                e = len(arr)-1 
                while s <= e:
                    mid = s - (s-e)//2
                    if arr[mid] == v:
                        return 1
                    elif arr[mid] > v:
                        e = mid - 1 
                    else:
                        s = mid + 1 
                return 0
        
        for n in mat[0]: # go through each element in first row, and find the first (smallest) element in all the rows
            cnt = 1
            for arr in mat[1:]:
                cnt += binFind(n, arr)
            if cnt == len(mat):
                return n
        return -1
    
    


# previous solution

# class Solution:
#     def smallestCommonElement(self, mat: 'List[List[int]]') -> int:
#         if len(mat)==1: return mat[0][0]
#         else:
#             curr = mat[0]
#             common = mat[0] #take the first row as common, and compare with the following rows
#             for m in mat[1:]:
#                 curr = common
#                 common = []
#                 while curr and m: #keep popping the current list or the m, if the element is < than the other[0]
#                     while curr and m and curr[0] < m[0]:
#                         curr.pop(0)
#                     while curr and m and curr[0] == m[0]:
#                         common.append(curr.pop(0))
#                         m.pop(0)
#                     while curr and m and curr[0] > m[0]:
#                         m.pop(0)

#                 if common == []:
#                     return -1

#             return common[0]



# previous approach
# class Solution:
#     def smallestCommonElement(self, mat: 'List[List[int]]') -> int:
#         def overlap(A,B):
#             output = []
#             i = 0
#             while B: #B is the longer one
#                 if A == [] or B[0] > A[-1]: #in the sorted B and A, current B is larger than the max of A. No need to continue
#                     break
#                 elif B[0] > A[0]:
#                     A.pop(0)
#                 elif B[0] < A[0]:
#                     B.pop(0)
#                 else:
#                     output.append(A[0])
#                     A.pop(0)
#                     B.pop(0)
#             return output
#         output = []
#         if len(mat) ==1:
#             return mat[0][0]
#         else:
#             output = overlap(mat[0], mat[1])
#             c = 2
#             while c < len(mat):
#                 output = overlap(output, mat[c])
#                 if output == []: # no need to check the rest
#                     return -1
#                 c+=1
#             return -1 if output==[] else output[0]