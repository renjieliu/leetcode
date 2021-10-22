class Solution:
    def assignBikes(self, workers: 'List[List[int]]', bikes: 'List[List[int]]') -> int: #RL 20211022: Copied solution
        def calc_dist(i, j):
            worker, bike = workers[i], bikes[j]
            return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
        
        W, B = len(workers), len(bikes)
		#heap contains (sum_of_distance_so_far, choice_of_bike_indexes_so_far)
        heap = [(0, [])]
		#to avoid double count
        memo = set()
        
        while True:
            cur_dist, taken = heapq.heappop(heap)
            if tuple(sorted(taken)) in memo: 
                continue
            memo.add(tuple(sorted(taken)))
			#if we have taken bikes for everyone
            if len(taken) == W:
                break
            cur_idx = len(taken)
            for new_idx in range(B):
                if new_idx not in taken:
                    new_dist = calc_dist(cur_idx, new_idx)
                    heapq.heappush(heap, (cur_dist + new_dist, taken + [new_idx]))
        
        return cur_dist

    
        
        
# my approach, TLE
# class Solution:
#     def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
#         def perm(output, dist, loc, arr, bikes, workers): # permutation all bikes, to assign different bikes to worker
#             if loc == len(workers):
#                 #print(path, dist)
#                 output[0] = min(output[0], dist)                   
#             else:
#                 for i in range(len(arr)): # arr is the number of bikes . Perm(bikes, worker)
#                     b = arr[i]
#                     if dist < output[0]:
#                         t = dist + abs(bikes[b][0] - workers[loc][0]) + abs(bikes[b][1] - workers[loc][1])
#                         perm(output, t, loc+1, arr[:i] + arr[i+1:], bikes, workers)
                    
#         hmp = {} 
#         output = [float('inf')]
#         perm(output, 0, 0, tuple(range(len(bikes))), bikes, workers)
#         return output[0]
        
 