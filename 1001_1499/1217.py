class Solution:
    def minCostToMoveChips(self, position: 'List[int]') -> int:
        arr = [0,0] #odd, even
        for p in position:
            arr[p % 2]+=1 # either odd +1 or even +1 
        return min(arr) # return the min of the odd and even
    


# previous approach
# class Solution:
#     def minCostToMoveChips(self, position: 'List[int]') -> int:
#         odd = even = 0
#         for p in position:
#             if p%2==0:
#                 even +=1
#             else:
#                 odd+=1
#         return 0 if even*odd == 0 else min(even, odd)


# previous approach
# class Solution:
#     def minCostToMoveChips(self, chips: List[int]) -> int:
#         s1, s2  = 0, 0
#         for i in chips:
#             s1+= 0 if abs((i-1))%2 ==0 else 1  # move everything to position 1
#             s2+= 0 if abs((i - 2)) % 2 == 0 else 1 #move everything to position 2
#         return min(s1, s2)
