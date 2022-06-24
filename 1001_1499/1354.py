class Solution:
    def isPossible(self, target: 'List[int]') -> bool: #O(NlogN | N )
        if len(target) == 1:
            return target[0] == 1
        
        pq = []
        for t in target:
            heapq.heappush(pq, -t)
        
        total = sum(target)
        
        while -pq[0] > 1: # work backwards, to find how to reach current max
            mx = -pq[0]
            rest = total - mx 
            
            if rest == 1: #if rest is 1, it must be [1,xxxxx]
                return True
            
            #nxt = mx - rest #this is the prev number, turn to current mx # inefficient, if mx is very large
            nxt = mx % rest # it's reducing the same rest each time, until different occurrs. 
            
            # if nxt < 1: #if prev number has to be < 1 to reach current state, then return False
            #     return False
            
            if nxt == 0 or nxt == mx:
                return False
            
            heapq.heappop(pq) # pop current mx 
            heapq.heappush(pq, -nxt)  # push the previously replaced number
            
            total = total - mx + nxt
            
        return True
    
    

# previous solution

# class Solution:
#     def isPossible(self, target: 'List[int]') -> bool:
#         if len(target) == 1:
#             return target == [1]
#         total_sum = sum(target)
#         target = [-num for num in target]
#         heapq.heapify(target)
#         while -target[0] > 1:
#             largest = -target[0]
#             rest = total_sum - largest

#             # This will only occur if n = 2.
#             if rest == 1:
#                 return True

#             x = largest % rest

#             # If x is now 0 (invalid) or didn't
#             # change, then we know this is impossible.
#             if x == 0 or x == largest:
#                 return False
#             heapq.heapreplace(target, -x)
#             total_sum = total_sum - largest + x

#         return True


