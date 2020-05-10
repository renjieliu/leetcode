class Solution:
    def buildArray(self, target: 'List[int]', n: int) -> 'List[str]':
        output = []
        for i in range(1, n + 1):
            output.append("Push")
            if target[0] > i:
                output.append("Pop")
            else:
                target.pop(0)
                if target == []: return output
        return output
