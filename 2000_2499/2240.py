class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        cnt = 0 
        maxPen = total // cost1
        for pen in range(maxPen+1):
            cnt += ( (total - pen*cost1) // cost2 + 1) # with current amount of pen, how many pencils can be bought, including 0 pencils
        
        return cnt

    
