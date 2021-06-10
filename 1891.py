class Solution:
    def maxLength(self, ribbons: 'List[int]', k: int) -> int:
        if k > sum(ribbons):
            return 0
        ribbons.sort()
        def canCut(arr, k, length): # if arr can be cut to k ribbons with length >= length
            cnt = 0
            for a in arr[::-1]:
                cnt += a//length
                if cnt >= k:
                    break
            return cnt >= k

        def binFind(arr, k): #binary search to check if it can be cut into k currValue ribbons
            s = 1
            e = max(ribbons)
            output = 1
            while s <= e :
                mid = s - (s-e)//2
                if canCut(arr, k, mid):
                    output = max(output, mid)
                    s = mid + 1
                else:
                    e = mid -1
            return output

        return binFind(ribbons, k)





