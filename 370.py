class Solution:
    def getModifiedArray(self, length: int, updates: 'List[List[int]]') -> 'List[int]':
        output = [0] * (length +1)
        for s, e, v in updates:
            output[s] += v
            output[e+1] -= v
        for i in range(1, len(output)):
            output[i] += output[i-1]
        return output[:-1]