class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: 'List[List[int]]') -> int: # O( N**2 | N )
        dp = [startFuel] + [0] * len(stations) # dp to record the farmost place can reach from current station 
        for i, (location, fuel) in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= location:  # current location can be reached
                    dp[j+1] = max(dp[j+1], dp[j] + fuel)
        
        for i, reach in enumerate(dp): #to check dp, if from current can reach target, then just return the index 
            if reach>=target:
                return i
        
        return -1

    

# previous solution

# class Solution:
#     def minRefuelStops(self, target: int, startFuel: int, stations: 'List[List[int]]') -> int:
#         dp = [startFuel] + [0] * len(stations)
#         for i, (location, capacity) in enumerate(stations):
#             for t in range(i, -1, -1):
#                 if dp[t] >= location:
#                     dp[t+1] = max(dp[t+1], dp[t] + capacity)

#         for i, d in enumerate(dp):
#             if d >= target: return i
#         return -1

