class Solution:
    def getOrder(self, tasks: 'List[List[int]]') -> 'List[int]': # O( NlogN | N )
        tasks = sorted([ tasks[idx] + [idx] for idx in range(len(tasks))] )
        pq = []
        output = []
        curr_time = 0
        i = 0
        while i < len(tasks) or pq: # keep pushing valid tasks to the heap, and taking out the one with smallest duration and index
            if len(pq) == 0 and curr_time < tasks[i][0]: # need to update the current Time
                curr_time = tasks[i][0]
            
            while i < len(tasks) and curr_time >= tasks[i][0]:
                enqueue, duration, idx = tasks[i]
                heapq.heappush(pq, (duration, idx)) # heap sort with tuples for multiple dimension sort
                i += 1
            duration, idx = heapq.heappop(pq)
            # Complete this task and increment curr_time.
            curr_time += duration
            output.append(idx)
        
        return output 
    
    
