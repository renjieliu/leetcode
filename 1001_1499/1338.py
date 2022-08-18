class Solution:
    def minSetSize(self, arr: 'List[int]') -> int: # O( NlogN | N )
        total = len(arr) 
        hmp = {}
        for a in arr: # count the occurrence of each number
            if a not in hmp:
                hmp[a] = 0
            hmp[a] += 1 
        cnt = 0 
        lst = sorted(hmp.values())
        while total > len(arr)//2:  # start taking from the one with max occurrence.
            total -= lst.pop()
            cnt += 1
        return cnt
    



# previous solution

# class Solution:
#     def minSetSize(self, arr: 'List[int]') -> int:
#         hmp = {}
#         for a in arr:
#             if a not in hmp:
#                 hmp[a] = 0
#             hmp[a]+=1
#         curr = 0
#         cnt = 0
#         stk = sorted(hmp.values())
#         while curr < len(arr)//2:
#             curr += stk.pop() # pop from right to left, meaning popping from largest to smallest
#             cnt += 1
#         return cnt


# previous solution

# class Solution:
#     def minSetSize(self, arr: 'List[int]') -> int:
#         hmp = {}
#         for a in arr:
#             if a not in hmp:
#                 hmp[a] = 0
#             hmp[a] +=1
#         target = len(arr)//2  #(len(arr) +1)//2 # the length will be even per desc, for odd length, +1 //2 , for even length,+1//2 will not change the result
#         s = 0 
#         cnt = 0
#         lst = sorted(hmp.values(), reverse = True) # this value shows the occurrance of the number 
#         #print(lst)
#         for v in lst:
#             s+=v
#             cnt+=1
#             if s >=target:
#                 return cnt
        