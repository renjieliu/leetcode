class Solution:
    def finalValueAfterOperations(self, operations: 'List[str]') -> int:
        return sum(1 if "+" in _ else -1 for _ in operations)

