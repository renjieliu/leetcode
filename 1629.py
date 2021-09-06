class Solution:
    def slowestKey(self, releaseTimes: 'List[int]', keysPressed: str) -> str:
        prev = 0
        output = keysPressed[0]
        currMax = releaseTimes[0]
        for i in range(len(releaseTimes)):
            if releaseTimes[i] - prev > currMax:
                currMax = max(currMax, releaseTimes[i] - prev)
                output = keysPressed[i]
            elif releaseTimes[i] - prev == currMax:
                output = max(output, keysPressed[i])
            prev = releaseTimes[i]
        return output




# previous approach
# class Solution:
#     def slowestKey(self, releaseTimes: 'List[int]', keysPressed: str) -> str:
#         curr = releaseTimes[0]
#         output = keysPressed[0]
#         for i in range(1, len(keysPressed)):
#             diff = releaseTimes[i] - releaseTimes[i - 1]
#             if diff > curr:
#                 curr = diff
#                 output = keysPressed[i]
#             elif diff == curr:
#                 output = max(keysPressed[i], output)
#         return output
#

