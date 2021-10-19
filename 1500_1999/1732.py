class Solution:
    def largestAltitude(self, gain: 'List[int]') -> int:
        output = 0
        curr = 0
        for g in gain:
            curr+=g
            output = max(curr, output)
        return output