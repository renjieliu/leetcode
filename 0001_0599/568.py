class Solution:
    def maxVacationDays(self, flights: 'List[List[int]]', days: 'List[List[int]]') -> int: #RL 20211231: Copied solution 
        N, K = len(days), len(days[0])
        best = [-float('inf')] * N
        best[0] = 0

        for t in range(K):
            cur = [-float('inf')] * N
            for i in range(N):
                for j, adj in enumerate(flights[i]):
                    if adj or i == j:
                        cur[j] = max(cur[j], best[i] + days[j][t])
            best = cur
        return max(best)
    
