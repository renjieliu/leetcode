class Solution:
    def maxNumberOfApples(self, arr: 'List[int]') -> int:
        arr.sort()
        s = 0
        cnt = 0
        for a in arr:
            s+=a
            if s <= 5000:
                cnt += 1
            else:
                return cnt
        return cnt