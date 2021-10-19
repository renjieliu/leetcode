class KthLargest:

    def __init__(self, k: int, nums: 'List[int]'):
        self.k = k
        self.pq = []
        heapq.heapify(self.pq)
        for n in nums:
            if len(self.pq) < k:
                heapq.heappush(self.pq, n)
            else:
                heapq.heappushpop(self.pq, n) #push it and pop


    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heapq.heappush(self.pq, val)
        else:
            heapq.heappushpop(self.pq, val)

        return self.pq[0]  # kth largest is the smallest item in the length K pq.





# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# previous approach
# class KthLargest:
#
#     def __init__(self, k: int, nums: 'List[int]'):
#         self.k = k
#         self.nums = sorted(nums)
#
#
#     def add(self, val: int) -> int:
#         def binFind(arr, v): # to find the location to insert v into arr
#             if arr == [] or v < arr[0]:
#                 return 0
#             elif v > arr[-1]:
#                 return len(arr)
#             else:
#                 s = 0
#                 e = len(arr)-1
#                 output = -1
#                 while s <= e:
#                     mid = (s+e)//2
#                     if arr[mid] <= v:
#                         output = max(output, mid)
#                         s = mid + 1
#                     else:
#                         e = mid -1
#                 return output+1
#
#         loc = binFind(self.nums, val)
#         self.nums.insert(loc, val)
#         return self.nums[-self.k]
#
#
#
# # Your KthLargest object will be instantiated and called as such:
# # obj = KthLargest(k, nums)
# # param_1 = obj.add(val)