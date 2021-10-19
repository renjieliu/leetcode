class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        hmp = defaultdict(int)
        for i in range(lowLimit,highLimit+1):
            hmp[sum( [int(_) for _ in list(str(i)) ] )]+=1
        return max(hmp.values())