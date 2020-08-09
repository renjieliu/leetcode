class Solution:
    def findKthPositive(self, arr: 'List[int]', k: int) -> int:
        curr = 1
        cnt = 0
        while cnt < k:
            if arr and curr == arr[0]:
                arr.pop(0)
            else:
                cnt += 1
                if cnt == k:
                    return curr
            curr += 1
