class Solution:
    def minOperations(self, logs: 'List[str]') -> int:
        output = 1 if logs[0] not in ["./", "../"] else 0
        for i in logs[1:]:
            if i == "../":
                output -= 1 if output > 0 else 0
            elif i != "./":
                output += 1
        return output