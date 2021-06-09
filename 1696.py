class Solution:
    def maxResult(self, nums: 'List[int]', k: int) -> int:
        pq = []
        curr = nums[-1] #curr is the nums[i] + prev Max in the window
        heapq.heappush(pq, [-nums[-1], len(nums)-1]) #the max is to be at the top of the heap [currMax, pos]
        for i in range(len(nums)-2, -1, -1):
            while pq[0][1] > i + k:
                heapq.heappop(pq)
            curr = -pq[0][0] + nums[i] #the max up to now
            heapq.heappush(pq, [-curr, i])
        return curr


