class Solution:
    def kWeakestRows(self, mat: 'List[List[int]]', k: int) -> 'List[int]': #O(nlogn | n)
        def binFindCalc(arr): # return the sum of all the 1's
            s = 0 
            e = len(arr)-1
            output = -1 # if nothing find, output will be 0
            while s <= e:
                mid = s - (s-e)//2
                if arr[mid] == 1:
                    s = mid + 1
                    output = mid
                else:
                    e = mid - 1
            return output + 1 #return the sum of 1's 
        
        bucket = [[] for i in range(len(mat[0])+1)] #bucket sort to reduce the sort complexity
        
        for i, r in enumerate(mat):
            b = binFindCalc(r) 
            bucket[b].append(i)
        
        output = []
        for b in bucket:
            output += b
            if len(output)>=k:
                return output[:k]
            




# previous approach

# class Solution:
#     def kWeakestRows(self, mat: 'List[List[int]]', k: int) -> 'List[int]':
#         arr = []
#         for i in range(len(mat)):
#             curr = 0
#             arr.append([i])
#             for c in mat[i]:
#                 if c == 1:
#                     curr+=c
#                 else:
#                     break
#             arr[-1].append(curr)
#         arr.sort(key = lambda x: [x[1], x[0]])
#         output = []
#         #print(arr)
#         for i in range(k):
#             output.append(arr[i][0])
#         return output


# previous approach

# class Solution:
#     def kWeakestRows(self, mat: 'List[List[int]]', k: int) -> 'List[int]':
#         hmp = {} 
#         for r in range(len(mat)):
#             s = 0 
#             c = 0
#             while c < len(mat[r]):
#                 if mat[r][c]==1:
#                     s+=mat[r][c] 
#                 else:
#                     break
#                 c+=1
#             if s not in hmp:
#                 hmp[s] = []
#             hmp[s].append(r)
#         output  =[] 
#         lst = sorted(hmp.keys())
#         for i in lst :
#             for r in hmp[i]:
#                 output.append(r)
#         return output[:k]
            



