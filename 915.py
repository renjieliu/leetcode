class Solution:
    def partitionDisjoint(self, A: 'List[int]') -> int:
        leftMax = []
        currMax = -float('inf')
        for i, c in enumerate(A):
            currMax = max(c, currMax)
            leftMax.append(currMax)

        currMin = float('inf')
        rightMin = [0] * len(A)
        for i in range(len(A) - 1, -1, -1):
            currMin = min(currMin, A[i])
            rightMin[i] = currMin

        # print(leftMax)
        # print(rightMin)
        for i in range(len(A) - 1):
            if leftMax[i] <= rightMin[i + 1]: #if maxup to now is <= the min on the right.
                return i + 1
        return len(A) - 1