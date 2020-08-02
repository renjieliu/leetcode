class Solution:
    def getWinner(self, arr: 'List[int]', k: int) -> int:
        if k >= len(arr):
            return max(arr)
        else:
            cnt = 0
            curr = arr[0]
            for a in arr[1:]: #check how many times the element can win. If no element satisfy the condition, simply return the largest.
                if a > curr:
                    cnt = 0
                    curr = a
                cnt += 1
                if cnt == k:
                    return curr
            return curr
