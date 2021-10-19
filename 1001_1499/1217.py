class Solution:
    def minCostToMoveChips(self, position: 'List[int]') -> int:
        odd = even = 0
        for p in position:
            if p%2==0:
                even +=1
            else:
                odd+=1
        return 0 if even*odd == 0 else min(even, odd)