class Solution:
    def minimumCost(self, cost: 'List[int]') -> int:
        output = 0 
        cost.sort()
        while cost:
            output += cost.pop() #buy the current most expensive one
            if cost:
                output+=cost.pop() #buy the current most expensive one
            if cost:
                cost.pop() #take the one for fre
        
        return output
    
