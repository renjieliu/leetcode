class Solution:
    def lastStoneWeight(self, stones: 'List[int]') -> int:
        stones.sort()
        if len(stones) == 1: return stones[0]
        while stones:
            if stones[-2] == stones[-1]:
                stones = stones[:-2]
            else:
                i = 0
                while i < len(stones[:-2]):  # find the stone loc after collision
                    if stones[i] > stones[-1] - stones[-2]:
                        break
                    i += 1
                stones = stones[:i] + [stones[-1] - stones[-2]] + stones[i:-2]

            if len(stones) == 1:
                return stones[0]
        return 0