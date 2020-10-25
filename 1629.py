class Solution:
    def slowestKey(self, releaseTimes: 'List[int]', keysPressed: str) -> str:
        curr = releaseTimes[0]
        output = keysPressed[0]
        for i in range(1, len(keysPressed)):
            diff = releaseTimes[i] - releaseTimes[i - 1]
            if diff > curr:
                curr = diff
                output = keysPressed[i]
            elif diff == curr:
                output = max(keysPressed[i], output)
        return output


