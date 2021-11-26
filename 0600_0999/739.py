class Solution:
    def dailyTemperatures(self, temperatures: 'List[int]') -> 'List[int]':
        output = [0 for _ in temperatures]
        stk = []  # monotone stk.
        for i in range(len(temperatures)-1, -1, -1):
            while stk and temperatures[i] >= temperatures[stk[-1]]: # keep popping the ones <= current temp
                stk.pop()
            if stk and temperatures[stk[-1]] > temperatures[i]: # if the stack top temperature is > current temp
                output[i] = stk[-1]-i
            
            stk.append(i)
        
        return output
    


# previous approach
# class Solution:
#     def dailyTemperatures(self, temperatures: 'List[int]') -> 'List[int]':
#         output = [0] * len(temperatures)
#         stk = []
#         for i in range(len(temperatures)-1, -1, -1):
#             while stk and temperatures[stk[-1]] <= temperatures[i]: # following <= curr, no need to check
#                 stk.pop()
#             if stk:
#                 output[i] = stk[-1] - i
            
#             stk.append(i)
#         return output
    
    



# previous approach
# class Solution:
#     def dailyTemperatures(self, temperatures: 'List[int]') -> 'List[int]':
#         output = [0 for _ in range(len(temperatures))] 
#         stk = [] 
#         for i in range(len(temperatures)-1, -1, -1):
#             while stk and temperatures[stk[-1]] <= temperatures[i]: #pop the ones on the right with <= curr
#                 stk.pop()
#             if stk:
#                 output[i] = stk[-1] - i
#             stk.append(i)
#         return output
        
       
        
        
# the heap approach        
#         output = [0 for _ in range(len(temperatures))]
#         pq = []
#         heapq.heapify(pq)
#         heapq.heappush(pq, [temperatures[0], 0]) #heap with [temp, idx]
#         for i in range(1, len(temperatures)):
#             while pq and temperatures[i] > pq[0][0]:
#                 t, idx = heapq.heappop(pq)
#                 output[idx] = i-idx #corresponding waiting days in the output array
#             heapq.heappush(pq, [temperatures[i], i])
        
#         return output





# previous approach 
# class Solution:
#     def dailyTemperatures(self, temperatures: 'List[int]') -> 'List[int]':
#         output = [0 for _ in range(len(temperatures))]
#         pq = []
#         heapq.heapify(pq)
#         heapq.heappush(pq, [temperatures[0], 0]) #heap with [temp, idx]
#         for i in range(1, len(temperatures)):
#             while pq and temperatures[i] > pq[0][0]:
#                 t, idx = heapq.heappop(pq)
#                 output[idx] = i-idx #corresponding waiting days in the output array
#             heapq.heappush(pq, [temperatures[i], i])
        
#         return output




# previous approach
# def dailyTemperatures(T: 'List[int]'):
#     curr_greater = []
#     output = [0]*len(T)
#     for i in range(len(T)-1, -1, -1):
#         while len(curr_greater)!=0 and T[curr_greater[-1]]<=T[i]:
#             curr_greater.pop()
#         if len(curr_greater)!=0:
#             output[i] = curr_greater[-1] - i
#         curr_greater.append(i)

#     return output

# print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))