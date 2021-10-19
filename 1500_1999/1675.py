class Solution:
    def minimumDeviation(self, nums: 'List[int]') -> int:
        # since heapq is a min-heap
        # we use negative of the numbers to mimic a max-heap
        evens = []
        minimum = float('inf')
        for num in nums:
            if num % 2 == 0:
                evens.append(-num)
                minimum = min(minimum, num)
            else:
                evens.append(-num*2)
                minimum = min(minimum, num*2)
        heapq.heapify(evens)
        min_deviation = float('inf')
        while evens:
            current_value = -heapq.heappop(evens)
            min_deviation = min(min_deviation, current_value-minimum)
            if current_value % 2 == 0:
                minimum = min(minimum, current_value//2)
                heapq.heappush(evens, -current_value//2)
            else:
                # if the maximum is odd, break and return
                break
        return min_deviation