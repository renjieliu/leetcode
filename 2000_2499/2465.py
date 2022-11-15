class Solution:
    def distinctAverages(self, nums: 'List[int]') -> int: # O( NlogN | N )
        mi = []
        mx = [] 
        for n in nums:
            heapq.heappush(mx, -n)
            heapq.heappush(mi, n)
        
        cnt = 0 # to count how many letters are taken
        lkp = set()
        while cnt < len(nums): # keep taking the current mx and mi from mx heap and mi heap
            lkp.add( (-heapq.heappop(mx) + heapq.heappop(mi) ) /2 ) # (-maxHeap + minHeap)/2
            cnt += 2
        
        return len(lkp)
            
            
