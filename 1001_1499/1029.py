class Solution:
    def twoCitySchedCost(self, costs: 'List[List[int]]') -> int:
        arr = sorted(costs, key = lambda x : x[0] - x[1]) #smaller x[0] will be placed to the A city.
        L = len(costs)
        return sum(a for a, b in arr[:L//2]) + sum(b for a, b in arr[L//2:]) #1st half to be placed to city a, 2nd to city b




# previous approach

# class Solution:
#     def twoCitySchedCost(self, costs: 'List[List[int]]') -> int:
#         costs = sorted(costs, key = lambda x:x[0] - x[1])
#         return sum(map(lambda x: x[0], costs[:len(costs)//2])) + sum(map(lambda x: x[1], costs[len(costs)//2:]))


# previous approach
# class Solution:
#     def twoCitySchedCost(self, costs: 'List[List[int]]') -> int:
#         costs = sorted(costs, key= lambda x : x[0]- x[1] )
#         output = 0
#         cnt = 0
#         for i in range(len(costs)):
#             if cnt < len(costs)//2:
#                 output += costs[i][0]
#             else:
#                 output +=costs[i][1]
#             cnt += 1
#         return  output


