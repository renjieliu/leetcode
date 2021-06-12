class Solution:
    def isCovered(self, ranges: 'List[List[int]]', left: int, right: int) -> bool:
        cnt = 0
        for i in range(left, right+1):
            for a, b in ranges:
                if a<=i<=b:
                    cnt += 1
                    break
        return cnt == right-left+1

