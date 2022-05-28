class Solution:
    def networkDelayTime(self, times: 'List[List[int]]', n: int, k: int) -> int: #O(ElogN | N + E)
        hmp = defaultdict(lambda : [] )
        for a, b, t in times:
            hmp[a].append([t, b]) # [time for travel, neighbor node]
        
        pq = [[0, k]]
        heapq.heapify(pq)
        seen = set()
        while pq: # classic Dijkstra's algo, ElogN
            time, node = heapq.heappop(pq)
            seen.add(node)
            if len(seen) == n :
                return time
            for t, nxt in hmp[node]:
                if nxt not in seen:
                    heapq.heappush(pq, [t+time, nxt])
        return -1

    

# previous solution


# class Solution:
#     def networkDelayTime(self, times: 'List[List[int]]', n: int, k: int) -> int: #O((n-1)! + ElogE | N)
#         hmp = defaultdict(lambda: []) 
#         for a, b, t in times:
#             hmp[a].append([t, b])
        
#         seen = set()
#         pq = [[0, k]]
#         heapq.heapify(pq)
#         while pq:  # O((N-1)!), classic dijkstra's algo. Each time, push the current cost to the heap, and take out the least cost for the next round
#             time, node = heapq.heappop(pq)
#             seen.add(node)
#             if len(seen) == n:
#                 return time
#             else:
#                 for nxt_time, nxt_node in hmp[node]: #ElogE
#                     if nxt_node not in seen:
#                         heapq.heappush(pq, [nxt_time + time, nxt_node])
        
#         return -1 
    

        
