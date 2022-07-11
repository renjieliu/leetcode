class Solution:
    def maxResult(self, nums: 'List[int]', k: int) -> int: # O( NlogN | N)
        pq = [[-nums[-1], len(nums)-1]] #initialize the pq with the last number, [num, loc]
        heapq.heapify(pq)
        output = -pq[0][0]
        for i in range(len(nums)-2, -1, -1): 
            while pq and pq[0][1] > i+k: # keep removing the item from the heap, as if it's out of range
                heapq.heappop(pq) 
            output = nums[i]-pq[0][0] # max from current 
            heapq.heappush(pq, [-output, i]) # push back to the heap
        return output
    
    

# class Solution:
#     def maxResult(self, nums: 'List[int]', k: int) -> int:
#         pq = []
#         curr = nums[-1] #curr is the nums[i] + prev Max in the window
#         heapq.heappush(pq, [-nums[-1], len(nums)-1]) #the max is to be at the top of the heap [currMax, pos]
#         for i in range(len(nums)-2, -1, -1):
#             while pq[0][1] > i + k:
#                 heapq.heappop(pq)
#             curr = -pq[0][0] + nums[i] #the max up to now
#             heapq.heappush(pq, [-curr, i])
#         return curr


